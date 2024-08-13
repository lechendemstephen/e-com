from django.contrib import admin

from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin): 
    list_display = ('username', 'is_active', 'is_superuser', 'last_login')





admin.site.register(CustomUser, CustomUserAdmin)