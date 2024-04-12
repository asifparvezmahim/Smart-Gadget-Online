from django.shortcuts import render, redirect
from decimal import Decimal
from balance.models import Balance
from .models import Deposit


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
        return redirect("depo_form")
    return render(request, "deposite_form.html")


# def depo_history(request):
