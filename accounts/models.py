from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True) 
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
