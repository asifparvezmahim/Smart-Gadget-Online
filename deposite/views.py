from django.shortcuts import render, redirect
from decimal import Decimal
from balance.models import Balance
from .models import Deposit
from django.contrib import messages


# Create your views here.
def depo_form(request):
    if request.method == "POST":
        user = request.user
        str_deposite_ammount = request.POST.get("amount")
        dec_deposite_ammount = Decimal(str_deposite_ammount)
        balance = Balance.objects.get(user=user).balance
        new_balance = dec_deposite_ammount + balance
        Balance.objects.filter(user=user).update(balance=new_balance)
        Deposit.objects.create(user=user, deposit_amount=str_deposite_ammount).save()
        messages.success(
            request, f"{dec_deposite_ammount} Taka Deposite To Your Account"
        )
        return redirect("depo_form")
    return render(request, "deposite_form.html")


# def depo_history(request):
