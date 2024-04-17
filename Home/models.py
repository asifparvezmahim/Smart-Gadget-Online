from django.db import models


# Create your models here.
class SliderImage(models.Model):
    image = models.ImageField(upload_to="Home/banner_images/")

    def __str__(self) -> str:
        return f"{self.id} banner_image"
