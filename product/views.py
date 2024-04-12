from django.shortcuts import render
from .models import product_info


# Create your views here.
def diplay_products(request):
    products = product_info.objects.all()
    return render(request, "display_product.html", {"products": products})


def details_page(request, id):
    selected_product = product_info.objects.get(id=id)
    prd_image = selected_product.image
    prd_name = selected_product.name
    prd_details = selected_product.details
    prd_cat = selected_product.category.all()  # multiple cat
    prd_price = selected_product.price
    prd_delCharge = selected_product.delevary_charge
    prd_discount = selected_product.discount
    available_quantity = selected_product.total_available_quantity
    print(prd_details)
    return render(
        request,
        "product_details.html",
        {
            "id": id,
            "cat": prd_cat,
            "prd_name": prd_name,
            "image": prd_image,
            "prd_details": prd_details,
            "prd_price": prd_price,
            "prd_delCharge": prd_delCharge,
            "prd_discount": prd_discount,
            "available": available_quantity,
        },
    )
