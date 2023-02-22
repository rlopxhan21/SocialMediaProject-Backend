from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

class User(AbstractUser):
    imagefield = ResizedImageField(upload_to="users/", null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True, default=None)
    
    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').null = False


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']