from django.shortcuts import render, redirect
from django.contrib import messages
from product.models import product_info
from django.contrib.auth.models import User
from decimal import Decimal
from balance.models import Balance
from product.models import product_info
from .models import Purchased_Product
from cart.models import Cart
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


# Create your views here.
def purchased_product_from_product_section(request, id):
    user = request.user
    product = product_info.objects.get(id=id)
    available_product = Decimal(
        product_info.objects.get(id=id).total_available_quantity
    )
    product_price = Decimal(product_info.objects.get(id=id).price)
    product_discount = Decimal(product_info.objects.get(id=id).discount)
    product_delivary = Decimal(product_info.objects.get(id=id).delevary_charge)
    get_discount = (product_price * product_discount) / Decimal(100)
    total_payment = product_price - get_discount + product_delivary
    user_balance = Decimal(Balance.objects.get(user=user).balance)
    if (user_balance >= product_price) and (available_product > 0):
        Purchased = Purchased_Product.objects.create(user=user, product=product)
        Purchased.save()
        new_available_product = available_product - Decimal(1)
        new_available_product = str(new_available_product)
        product_info.objects.filter(id=id).update(
            total_available_quantity=new_available_product
        )
        new_user_balance = user_balance - total_payment
        Balance.objects.filter(user=user).update(balance=new_user_balance)

    elif available_product <= 0:
        # product is not available
        pass

    else:
        print("Less Balance")
    return redirect("display_products")


def purchased_product_from_details_section(request, id):
    user = request.user
    user_balance = Decimal(Balance.objects.get(user=user).balance)
    selected_cart = Cart.objects.get(id=id)
    product_from_selected_cart = selected_cart.product
    available_product = Decimal(product_from_selected_cart.total_available_quantity)
    product_price = product_from_selected_cart.price
    discount = product_from_selected_cart.discount
    del_charge = product_from_selected_cart.delevary_charge
    get_discount = (product_price * discount) / Decimal(100)
    total_payment = product_price - get_discount + del_charge
    user_balance = Decimal(Balance.objects.get(user=user).balance)
    if (user_balance >= product_price) and (available_product > 0):
        Purchased = Purchased_Product.objects.create(
            user=user, product=product_from_selected_cart
        )
        Purchased.save()
        new_available_product = available_product - Decimal(1)
        new_available_product = str(new_available_product)
        #
        # print("From 65 : ", selected_cart.product.pk)
        new_available_product = Decimal(available_product) - Decimal(1)
        product_info.objects.filter(id=selected_cart.product.pk).update(
            total_available_quantity=new_available_product
        )
        new_user_balance = user_balance - total_payment
        Balance.objects.filter(user=user).update(balance=new_user_balance)
        selected_cart.delete()

    print("Cart : ", del_charge)
    return redirect("homepage")
