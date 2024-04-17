from django.shortcuts import render, redirect
from product.models import product_info
from .models import SliderImage
from product.models import product_info


# Create your views here.
def home(request):
    prd = product_info.objects.all()
    images = SliderImage.objects.all()
    demos = product_info.objects.all()[:5]
    return render(request, "home.html", {"prds": prd, "images": images, "demos": demos})


def load_all(request):
    if request.user.is_authenticated:
        return redirect("display_products")
    else:
        return redirect("user_login")
