from django.shortcuts import render, redirect
from product.models import product_info
from .models import Cart
from django.contrib import messages


# Create your views here.
# add cart button on product showin
def myCart(request, id):
    id = id
    user = request.user
    if user.is_authenticated:
        product = product_info.objects.get(id=id)

        # Convert values to appropriate types
        price = product.price
        delivery_charge = product.delevary_charge
        discount = product.discount

        total = (
            price - (price * (discount / 100)) + delivery_charge
        )  # No need to convert to int

        # Create and save the Cart object
        cart = Cart.objects.create(
            user=user,
            product=product,
            price=price,
            delevary_charge=delivery_charge,  # delevary_charge
            discount=discount,
            total=total,
        )

        cart.save()
        messages.success(
            request,
            "The Product is Added Successfully to Your Cart.Check It to Your Cart",
        )
        return redirect("display_products")
    else:
        return redirect("user_login")


def go_to_cart(request):
    user = request.user
    myCarts = Cart.objects.filter(user=user)
    return render(request, "cart.html", {"carts": myCarts})


def delete_from_cart(request, id):
    selectedCart = Cart.objects.get(id=id)
    selectedCart.delete()
    return redirect("go_to_my_cart")
