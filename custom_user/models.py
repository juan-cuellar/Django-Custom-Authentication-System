from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):

    '''
    The User model has a custom manager that has the following helper 
    methods (in addition to the methods provided by BaseUserManager):

    '''

    def _create_user(self, email, password, **extra_fields): 

        ''' 
        The extra_fields keyword arguments are passed through to the 
        User's __init__ method to allow setting arbitrary fields on a custom 
        user model.
        '''

        if not email:
            raise ValueError("Users must have an email address")

        email=self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=150, blank=True, default='', unique=True)
    name = models.CharField(max_length=150, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    oblects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'users'
    

    def get_full_name(self): 
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
