from django.shortcuts import render
from product.models import product_info


# Create your views here.
def home(request):
    prd = product_info.objects.all()
    return render(request, "home.html", {"prds": prd})
