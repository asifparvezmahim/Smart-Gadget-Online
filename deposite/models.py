from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit_amount = models.CharField(max_length=20)
    date_time_field = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Deposites {self.deposit_amount}"
