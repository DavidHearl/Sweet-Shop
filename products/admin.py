from types import CellType
from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'color',
        'flavour',
        'vegetarian',
        'rating',
        'brand',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
