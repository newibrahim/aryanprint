from django.contrib import admin
from .models import Product, Offer, Seafood, Fruits, Veg, HomeProducts


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class SeafoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class VegAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class HomeProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Seafood, SeafoodAdmin)
admin.site.register(Fruits, FruitAdmin)
admin.site.register(Veg, VegAdmin)
admin.site.register(HomeProducts, HomeProductsAdmin)

