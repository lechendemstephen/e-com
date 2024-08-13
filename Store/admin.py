from django.contrib import admin
from .models import Products, Review, Category
# Register your models here.



# register the models to the admin backend

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('title', 'sale_price', 'discount_price' , 'category', 'reviews', 'slug', 'description', 'added_date', )
    prepopulated_fields = {
        'slug': ('title',)
    }

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'image',  'description', 'created_date')


class ReviewAdmin(admin.ModelAdmin): 
    list_display = ('review', 'rating', 'created_date')






admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)

