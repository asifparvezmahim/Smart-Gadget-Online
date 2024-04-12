from django.contrib import admin
from .models import Purchased_Product, invoice

# Register your models here.
admin.site.register(Purchased_Product)
admin.site.register(invoice)
