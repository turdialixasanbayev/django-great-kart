from django.db import models

# from django.db.models import Avg, Count

from django.utils.text import slugify
from django.urls import reverse

# from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True, null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Product(BaseModel):
    """
    Product model
    """

    class PriceType(models.TextChoices):
        UZS = "UZS", "so'm"
        RUB = "RUB", "₽"
        USD = "USD", "$"

    name = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_type = models.CharField(
        max_length=3,
        choices=PriceType.choices,
        default=PriceType.UZS,
    )
    description = models.TextField(null=True, blank=True)
    percentage = models.PositiveSmallIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    @property
    def discount_price(self):
        if self.percentage:
            return self.price - (self.price * self.percentage / 100)
        return self.price

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
        ]

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
