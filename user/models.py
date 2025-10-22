from django.db import models

from django.utils import timezone

from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    User Model
    """

    # groups = None
    # user_permissions = None

    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    email = models.EmailField(unique=True, db_index=True)
    phone_number = PhoneNumberField(max_length=25, region="UZ", unique=True)

    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="users",
        blank=True,
        null=True,
    )
    bio = RichTextField(
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
    )

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_number"]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["phone_number"]),
        ]

    @property
    def age(self):
        if self.birth_date:
            today = timezone.now().date()
            age = today.year - self.birth_date.year
            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1
            return age
        return None

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.email:
            return f"{self.email}"
        if self.phone_number:
            return f"{self.phone_number}"
        return f"{self.username}"
