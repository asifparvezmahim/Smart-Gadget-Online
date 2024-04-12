from django.db import models
from django.contrib.auth.models import User
from product.models import product_info


# Create your models here.
class Purchased_Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_info, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Purchased {self.product.name} "


class invoice(models.Model):
    pdf_file = models.FileField(upload_to="invoices/", null=True, blank=True)
    purchased_product = models.OneToOneField(
        Purchased_Product, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Invoice for Parchesing ID : {self.purchased_product.pk}"
