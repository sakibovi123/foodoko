from audioop import add
from email import message
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from authentication.models import DriverProfile, VendorProfile
# Create your views here.

class RegistrationView(View):
    template_name = "auth/register.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_exists = User.objects.filter(username=username)

        if username != '' and email != '' and password != '':
            if user_exists.exists():
                messages.error(request, "The username already exists!")
                return redirect("registrationView")
            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                return redirect("loginView")


class LoginView(View):
    template_name = "auth/login.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")


class VendorSetupView(View):
    template_name = "vendorAuth/vendor_setup.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            user = request.user
            vendor_name = request.POST.get("vendor_name")
            shop_name = request.POST.get("shop_name")
            shop_logo = request.FILES.get("shop_logo")
            contact_name = request.POST.get("contact_name")
            address = request.POST.get("address")

            if user is not None:
                vendor = VendorProfile(
                    vendor_name=vendor_name,
                    shop_name=shop_name,
                    shop_logo=shop_logo,
                    contact_name=contact_name,
                    address=address
                )
                vendor.save()
                return redirect(f"/")


class DriverSetupView(View):
    template_name = "driverAuth/driver_setup.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            user =request.user
            full_name = request.POST.get("full_name")
            contact_name = request.POST.get("contact_name")
            photo = request.FILES.get("photo")
            driving_license_photo = request.FILES.get("driving_license_photo")
            address = request.POST.get("address")

            if user is not None:
                driver = DriverProfile(
                    user=user,
                    full_name=full_name,
                    contact_name=contact_name,
                    photo=photo,
                    driving_license_photo=driving_license_photo,
                    address=address
                )
                driver.save()
                return redirect(f"/")
            else:
                message.warning(request, "Something went wrong")