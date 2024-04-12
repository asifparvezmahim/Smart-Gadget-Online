from django.db import models
from Category.models import Product_Category


# Create your models here.
class product_info(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product/images/")
    details = models.TextField(max_length=500)
    category = models.ManyToManyField(Product_Category)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    delevary_charge = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2, default=0
    )
    discount = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="In Percentage",
    )
    total_available_quantity = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
