from django.contrib import admin

from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','author','in_stock','created','slug','price']
    list_filter=['in_stock','is_active']
    list_editable=['in_stock']
    prepopulated_fields={'slug':('title',)}
    

