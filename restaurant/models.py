from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "dish type"
        verbose_name_plural = "dish types"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(decimal_places=1, max_digits=4, blank=False)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="cooks")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name
