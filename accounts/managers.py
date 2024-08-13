from django.contrib.auth.base_user import BaseUserManager




class CustomUserManager(BaseUserManager): 


    def create_user(self, email, password, **extra_fields): 
        if not email: 
            raise ValueError('User must enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user 
    
    def create_superuser(self, email, password, **extrafields): 
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)

        if extrafields.get('is_staff') is not True:

            raise ValueError('superuser must have staff True')
        

        if extrafields.get('is_superuser') is not True:


            raise ValueError('superuser must have superuser True')
        

        if extrafields.get('is_active') is not True:


            raise ValueError('superuser must have active True')
        
        return self.create_user(email, password, **extrafields)