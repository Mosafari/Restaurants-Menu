from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):

    username = None
    name = models.CharField(max_length=100, unique=True)
    restaurant =models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []#'name']

    def __str__(self):
        return self.name
    
