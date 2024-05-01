from django.contrib import admin

from .models import ProductType, Product


class ProductInLine(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine,]

    search_fields = ['name',]
    list_display = ['name',]
    list_filter = ['name',] 


class ProductAdmin(admin.ModelAdmin):
    model = Product

    search_fields = ['name',]
    list_display = ['name', 'price','product_type',]
    list_filter = ['name','price','product_type',] 

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)