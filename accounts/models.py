from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    id = models.AutoField(blank=False, primary_key=True)
    age = models.CharField(blank=False, max_length=50)
    tel = models.CharField(blank=False, max_length=50)
    address = models.CharField(blank=False, max_length=50)
    style = models.CharField(blank=False, max_length=50)
    postal_code = models.CharField(blank=False, max_length=50)
    email = models.CharField(blank=False, max_length=50)

