import json
import requests
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import generic
from decouple import config

# Create your views here.

CAPTCHA_SITE_KEY = config('CAPTCHA_SITE_KEY')
def ShowLoginPage(request):
    return render(request, "registration/authentication.html", {'CAPTCHA_SITE_KEY': CAPTCHA_SITE_KEY})


def doLogin(request):
    if request.method != "POST":
        return render(request, 'registration/authentication.html', {'PageTitle': 'Login Page'})

    else:
        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = config('CAPTCHA_SECRET_KEY')
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        if cap_json['success'] == False:
            messages.error(request, "Invalid Captcha Try Again")
            return redirect("do_login")
        user = auth.authenticate(request, username=request.POST.get(
            "username"), password=request.POST.get("password"))
        if user != None:
            auth.login(request, user)
            if user.user_type == "1":
                return redirect('admin_home')
            elif user.user_type == "2":
                return redirect("staff_home")
            else:
                return redirect("student_home")
        else:
            messages.error(request, "Invalid Login Details")
            return redirect("do_login")


def logout_user(request):
    auth.logout(request)
    return redirect("/")
