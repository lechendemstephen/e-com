
from django.shortcuts import render

# Create your views here.

def home(request): 

    return render(request, 'organicstore/pages/home.html')

def about(request): 

    return render(request, 'organicstore/pages/about.html')

def contact(request): 

    return render(request, 'organicstore/pages/contact.html')