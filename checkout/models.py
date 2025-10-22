from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

from store.models import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField('user.CustomUser', on_delete=models.CASCADE, related_name='cart_user')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    @property
    def items_count(self):
        return self.cart_item_cart.count()

    @property
    def cart_sub_total_price(self):
        return sum(item.product.price * item.quantity for item in self.cart_item_cart.all())

    @property
    def cart_total_price(self):
        return sum(item.product.discount_price * item.quantity for item in self.cart_item_cart.all())

    def __str__(self):
        return f"Cart ({self.user})"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_cart")
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, related_name='cart_item_product')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    @property
    def item_total_price(self):
        return self.product.discount_price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Order(BaseModel):
    STATUS = (
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='order_user')
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(max_length=25, region="UZ")
    address = models.CharField(max_length=225)
    notes = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.pk} - {self.first_name} {self.last_name}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item_order')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='order_item_product')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.price})"
