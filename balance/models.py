from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} has a balance of {self.balance}"
