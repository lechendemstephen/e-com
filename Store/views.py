from django.shortcuts import render, get_object_or_404
from .models import Products, Category
# Create your views here.


def store(request): 
    categories = None

    # if category_name != None: 
    #     categories = get_object_or_404(Category, name=category_name)
    #     cat_product = Products.objects.filter(category=categories)
        
    # else: 
    products =Products.objects.all().order_by('id')


    context = {
        'products': products, 
        'categories': Category.objects.all()
        
    }

    return render(request, 'organicstore/pages/store.html', context)

