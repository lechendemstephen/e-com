from django.urls import path

from . import views


urlpatterns = [

    path('', views.store, name='store'), 


    path('<slug:category_name>/', views.store, name='product_search')
    
]
