from django.shortcuts import render, redirect
from product.models import product_info
from productReview.models import ProductReview


# Create your views here.
def save_review(request, id):
    user = request.user
    selected_prd = product_info.objects.get(id=id)
    comment = request.POST.get("review")
    new_record = ProductReview.objects.create(
        user=user, product=selected_prd, comment=comment
    )
    new_record.save()
    return redirect("details", id=id)
