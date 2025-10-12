from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Cart Admin Interface.
    """

    model = Cart
    ordering = ('-id',)
    list_display = (
        'id',
        'user',
        'items_count',
        'cart_sub_total_price',
        'cart_total_price',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'items_count',
        'cart_sub_total_price',
        'cart_total_price',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'user',)
    list_per_page = 5
    list_filter = ('is_active',)
    search_fields = ('user__username',)
    autocomplete_fields = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    CartItem Admin Interface.
    """

    model = CartItem
    ordering = ('-created_at',)
    list_display = (
        'id',
        'cart',
        'product',
        'quantity',
        'item_total_price',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'item_total_price',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'cart',)
    list_per_page = 10
    list_filter = ('is_active',)
    search_fields = ('cart__user__username', 'product__name',)
    autocomplete_fields = ('cart', 'product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    OrderAdmin Interface.
    """

    model = Order
    ordering = ('created_at',)
    list_per_page = 5
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'user',
        'status',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'notes',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'user',)
    list_editable = ('status',)
    autocomplete_fields = ('user',)
    list_filter = ('status', 'is_active',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'notes',
    )


class OrderItemAdmin(admin.ModelAdmin):
    """
    OrderItemAdmin interface...
    """

    model = OrderItem
    ordering = ('-id',)
    date_hierarchy = 'updated_at'
    list_display_links = ('id', 'order',)
    list_per_page = 10
    list_display = (
        'id',
        'order',
        'product',
        'quantity',
        'price',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_editable = ('quantity',)
    autocomplete_fields = ('order', 'product',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'product__name',
        'order__first_name',
        'order__user__username',
    )
    list_filter = ('is_active',)


admin.site.register(OrderItem, OrderItemAdmin)
