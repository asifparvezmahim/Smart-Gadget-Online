from django.db import models
from product.models import product_info
from django.contrib.auth.models import User


# Create your models here.
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        product_info, on_delete=models.CASCADE, related_name="reviews"
    )
    comment = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} Comment on {self.product.name}"
