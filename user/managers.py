from django.contrib.auth.models import UserManager

from django.core.exceptions import ValidationError

import re


class CustomUserManager(UserManager):
    """
    User Manager
    """

    def validate_email(self, email: str):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValidationError("Invalid email format!")
        return email

    def validate_phone(self, phone_number: str):
        pattern = r"^\+?\d{9,15}$"
        if not re.match(pattern, phone_number):
            raise ValidationError("Invalid phone number format!")
        return phone_number

    def create_user(self, username, email, phone_number, password, **extra_fields):
        if not username:
            raise ValueError("The username field is required.")
        if not email:
            raise ValueError("The email field is required.")
        if not phone_number:
            raise ValueError("The phone number field is required.")
        if not password:
            raise ValueError("The password field is required.")

        email = self.validate_email(email)
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username=username, email=email, phone_number=phone_number, password=password, **extra_fields)
