from django.contrib import admin
from .models import Category, Product





class CategoryAdmin(admin.ModelAdmin):
    list_display =  ('name', 'code')
    search_fields = ('name', 'code')
    

admin.site.register(Category, CategoryAdmin)

    
class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'quantity', 'category', 'code')
    search_fields = ('name', 'quantity', 'category', 'code')
    list_filter = ('name', 'quantity', 'category', 'code')
    

admin.site.register(Product, ProductAdmin)


