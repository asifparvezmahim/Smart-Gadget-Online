from django.db import models


# Create your models here.
class Product_Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, null=True, max_length=20, unique=True)

    def __str__(self):
        return self.name
