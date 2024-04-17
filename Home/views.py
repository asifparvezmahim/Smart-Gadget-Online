from django.shortcuts import render
from product.models import product_info
from .models import SliderImage
from product.models import product_info


# Create your views here.
def home(request):
    prd = product_info.objects.all()
    images = SliderImage.objects.all()
    demos = product_info.objects.all()[:5]
    return render(request, "home.html", {"prds": prd, "images": images, "demos": demos})
