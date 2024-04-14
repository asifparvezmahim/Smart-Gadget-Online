from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from balance.models import Balance
from decimal import Decimal
from deposite.models import Deposit
from django.http import JsonResponse
from purchased_product.models import Purchased_Product
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here


# def activateEmail(request, user, to_email):
#     messages.success(request, "emailCheckNotice.html")


def user_reg(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_email = request.POST.get("email")
        user_pass = request.POST.get("password1")
        user_conpass = request.POST.get("password2")

        if User.objects.filter(username=user_name).exists():
            return HttpResponse(
                "Username already exists. Please choose a different one."
            )
        else:
            if user_pass != user_conpass:
                return HttpResponse("Password and Confirm Pass Should be Same")
            else:
                user_info = User.objects.create_user(user_name, user_email, user_pass)
                user_info.is_active = False
                user_info.save()
                user = user_info
                balance = Decimal(0)
                balance_sheet = Balance.objects.create(user=user, balance=balance)
                balance_sheet.save()
                token = default_token_generator.make_token(user_info)
                uid = urlsafe_base64_encode(force_bytes(user_info.pk))
                confirm_link = f"http://127.0.0.1:8000/Accounts/active/{uid}/{token}"
                email_subject = "Registration Confirmation Email"
                email_body = render_to_string(
                    "reg_confirm_email.html", {"confirm_link": confirm_link}
                )
                email = EmailMultiAlternatives(email_subject, "", to=[user_info.email])
                email.attach_alternative(email_body, "text/html")
                email.send()
                messages.success(
                    request,
                    "We Sent an Email to Your E-Mail Address.Check It.If You Don't Get The Mail, Check Spam !!!!",
                )
                return redirect("homepage")

    return render(request, "reg.html")


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request,
            "Successfully Registration is Completed. Now You Can Log In To Your Account",
        )
        return redirect("homepage")
    else:
        return redirect("homepage")


def profile(request):
    user = request.user
    depo_hist = Deposit.objects.filter(user=user).order_by("-date_time_field")
    total_depo = Deposit.objects.filter(user=user).count()
    balance = Balance.objects.get(user=user).balance
    purchased_product = Purchased_Product.objects.filter(user=user)
    return render(
        request,
        "profile.html",
        {
            "user": user,
            "dipos": depo_hist,
            "bal": balance,
            "prods": purchased_product,
            "total_depo": total_depo,
        },
    )


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_pass = request.POST.get("pass")
        user_info = authenticate(username=user_name, password=user_pass)
        if user_info is not None:
            login(request, user_info)
            return redirect("homepage")
        else:
            return HttpResponse("Username or Pass is Incorrect")
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("user_login")
