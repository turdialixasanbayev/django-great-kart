from django.contrib import admin

from django.utils.html import mark_safe

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    User Admin Interface
    """
    model = CustomUser
    ordering = ('username',)
    date_hierarchy = 'date_joined'
    list_per_page = 5
    list_editable = ('username',)
    list_display = (
        'id',
        'get_full_name',
        'get_image',
        'first_name',
        'last_name',
        'username',
        'email',
        'phone_number',
        'gender',
        'birth_date',
        'age',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
    )
    filter_horizontal = (
        'groups',
        'user_permissions',
    )
    list_display_links = (
        'id',
        'get_full_name',
    )
    readonly_fields = (
        'id',
        'last_login',
        'date_joined',
        'age',
        'image_preview',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'gender',
    )
    search_fields = (
        'first_name',
        'last_name',
        'username',
        'email',
        'phone_number',
    )
    fieldsets = (
        ('Login', {
            'fields': ('username', 'password',),
            'classes': ('wide',),
        }),
        ("Personal Info", {
            'fields': ('first_name', 'last_name', 'email', 'phone_number',),
            'classes': ('wide',),
        }),
        ("Additional Info", {
            'fields': ('gender', 'image', 'bio', 'birth_date',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
            'classes': ('wide',),
        }),
        ("Groups and Permissions", {
            'fields': ('groups', 'user_permissions',),
            'classes': ('wide',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',),
        }),
        ("Age", {
            'fields': ('age',),
            'classes': ('wide', 'collapse',),
        }),
        ("Image", {
            'fields': ('image_preview',),
            'classes': ('wide', 'collapse',),
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'fields': ('username', 'email', 'phone_number',),
            'classes': ('wide',),
        }),
        ('Passwords', {
            'fields': ('password1', 'password2',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
            'classes': ('wide',),
        }),
        ("Groups and Permissions", {
            'fields': ('groups', 'user_permissions',),
            'classes': ('wide',),
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


admin.site.register(CustomUser, CustomUserAdmin)
