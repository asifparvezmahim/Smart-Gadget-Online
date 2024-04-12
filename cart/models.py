from django.db import models
from product.models import product_info
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(product_info, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    delevary_charge = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2
    )
    discount = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2
    )
    total = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    adding_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} -> {self.user.username}"
