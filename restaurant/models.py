from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]