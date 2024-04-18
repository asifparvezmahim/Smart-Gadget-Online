from django.shortcuts import render, redirect
from .models import product_info
from django.core.paginator import Paginator
from product.models import Product_Category
from productReview.models import ProductReview


# Create your views here.
def diplay_products(request, category_slug=None):
    products = product_info.objects.all()
    if category_slug is not None:
        category = Product_Category.objects.get(slug=category_slug)
        products = product_info.objects.filter(category=category)
    categories = Product_Category.objects.all()
    # set pagination
    p = Paginator(product_info.objects.all(), 6)  # Paginator (objects,per page object)
    page = request.GET.get("page")
    product = p.get_page(page)
    return render(
        request,
        "display_product.html",
        {"products": products, "product": product, "category": categories},
    )


def details_page(request, id):  # id=product_id
    selected_product = product_info.objects.get(id=id)
    prd_image = selected_product.image
    prd_name = selected_product.name
    prd_details = selected_product.details
    prd_cat = selected_product.category.all()  # multiple cat
    prd_price = selected_product.price
    prd_delCharge = selected_product.delevary_charge
    prd_discount = selected_product.discount
    available_quantity = selected_product.total_available_quantity
    review = ProductReview.objects.filter(product=selected_product)
    total_review = ProductReview.objects.filter(product=selected_product).count()
    return render(
        request,
        "product_details.html",
        {
            "selected_product": selected_product,
            "id": id,
            "cat": prd_cat,
            "prd_name": prd_name,
            "image": prd_image,
            "prd_details": prd_details,
            "prd_price": prd_price,
            "prd_delCharge": prd_delCharge,
            "prd_discount": prd_discount,
            "available": available_quantity,
            "review": review,
            "total_review": total_review,
        },
    )
