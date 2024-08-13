from django.db import models
from .managers import CustomUserManager

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): 
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()


    def __str__(self): 
        return self.email