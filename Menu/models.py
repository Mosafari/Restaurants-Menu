from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, restaurant, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        if not restaurant:
            raise ValueError('The Restaurant\'s Name must be set')
        restaurant = self.restaurant
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    restaurant = models.TextField(max_length=50,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['restaurant']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    categories = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    # add img to menu DB
    image = models.ImageField(upload_to='images') 
    
    def __str__(self):
        return self.name
    