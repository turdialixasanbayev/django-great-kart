from django.contrib import admin

from django.utils.html import mark_safe

# from django.contrib.auth.models import Group

from .models import Product, Category


admin.site.site_header = "Django GreatKart Admin Panel"
admin.site.site_title = "Django GreatKart Admin Panel"
admin.site.index_title = "Welcome to Django GreatKart Admin Panel"
admin.site.empty_value_display = "Not available"


# admin.site.unregister(Group)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin Interface...
    """

    model = Category
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = (
        'id',
        'name',
        'slug',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'slug',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_filter = ('is_active',)
    list_per_page = 10
    list_editable = ('slug',)
    fieldsets = (
        ("Personal Info", {
            'fields': ('name', 'slug',),
            'classes': ('wide',),
        }),
        ("Is active status", {
            'fields': ('is_active',),
            'classes': ('wide',),
        }),
        ("Important Dates", {
            'fields': ('created_at', 'updated_at',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',),
        }),
    )


class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin Interface...
    """

    model = Product
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_per_page = 5
    list_display_links = ('id', 'name',)
    list_display = (
        'id',
        'name',
        'slug',
        'category',
        'get_image',
        'price',
        'price_type',
        'percentage',
        'views_count',
        'discount_price',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'slug',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'image_preview',
        'discount_price',
    )
    list_filter = ('is_active', 'price_type',)
    list_editable = ('slug',)
    autocomplete_fields = ('category',)
    fieldsets = (
        ("Personal Info", {
            'fields': ('name', 'slug',),
            'classes': ('wide',),
        }),
        ("Additional Info", {
            'fields': ('category', 'image', 'description',),
            'classes': ('wide',),
        }),
        ("Price", {
            'fields': ('price', 'price_type', 'percentage',),
            'classes': ('wide',),
        }),
        ("Is active status", {
            'fields': ('is_active',),
            'classes': ('wide',),
        }),
        ("Views Count", {
            'fields': ('views_count',),
            'classes': ('wide',),
        }),
        ("Discount Price", {
            'fields': ('discount_price',),
            'classes': ('wide', 'collapse',),
        }),
        ("Image Preview", {
            'fields': ('image_preview',),
            'classes': ('wide', 'collapse',),
        }),
        ("Important Dates", {
            'fields': ('created_at', 'updated_at',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',),
        }),
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"

    get_image.short_description = "Image"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200" />')
        return "No image"

    image_preview.short_description = "Current Image"


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
