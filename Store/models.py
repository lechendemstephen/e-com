from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model): 
    title = models.CharField(max_length=150, null=False)
    sale_price = models.IntegerField()
    discount_price = models.IntegerField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    image =  models.ImageField(upload_to='products/')
    reviews = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='product_review')
    description = models.TextField(max_length=500, blank=False)
    slug = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)



    class Meta: 
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


    def __str__(self): 

        return self.title
   




class Category(models.Model): 
    name = models.CharField(max_length=150, null=False)
    image = models.ImageField(upload_to='category/',)
    description = models.TextField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta: 
        verbose_name = ' Category'
        verbose_name_plural = 'Categories'

    def __str__(self): 

        return self.name
    
    def get_url(self): 

        return reverse('product_search', args=[self.name])
    
 

class Review(models.Model): 
     review = models.TextField(max_length=500, null=False)
     rating = models.IntegerField()
     created_date = models.DateTimeField(auto_now_add=True)
     
     class Meta: 
          verbose_name = 'Review'
          verbose_name_plural = 'Reviews'

     def __str__(self): 
         
         return self.review