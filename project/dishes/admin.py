from django.contrib import admin
from django.contrib import admin
from dishes.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category')
    list_filter = ('category',)
    list_editable = ()
    search_fields = ('product_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', )
    list_filter = ()
    list_editable = ()
    search_fields = ('category_name',)


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
