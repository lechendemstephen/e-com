from django.shortcuts import render

# Create your views here.

def  sign_up(request): 

    return render(request, 'organicstore/pages/register.html' )



def  login(request): 

    return render(request, 'organicstore/pages/login.html' )