from django.contrib import admin

from django.contrib.auth.models import Group

from .models import Product, Review, Category


admin.site.site_header = "Django GreatKart Admin Panel"
admin.site.site_title = "Django GreatKart Admin Panel"
admin.site.index_title = "Welcome to Django GreatKart Admin Panel"
admin.site.empty_value_display = "Not available"


admin.site.unregister(Group)

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
