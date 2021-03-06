from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User
from datetime import date

from authentication.models import DriverProfile, VendorProfile

class Permission(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Permission"

    def __str__(self):
        return self.title


class Role(models.Model):
    created_at = models.DateField(default=date.today, null=True)
    role_title = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Role"
    
    def __str__(self):
        return f"Role title: {self.role_title}"


class Driver(models.Model):
    STATUS_CHOICE = (
        ("Active", "Active"),
        ("Closed", "Closed")
    )
    created_at = models.DateField(default=date.today)
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, default="Closed")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Driver"

    def __str__(self):
        return str(self.driver.full_name)


class Penalty(models.Model):
    STATUS_CHOICE = (
        ("Bann", "Bann"),
        ("Cancel Bann", "Cancel Bann"),
    )

    created_at = models.DateField(default=date.today)
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.driver.full_name



class Vehicle(models.Model):
    STATUS_CHOICE = (
        ("Active", "Active"),
        ("Closed", "Closed")
    )
    created_at = models.DateField(default=date.today)
    vehicle_type = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICE
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.vehicle_type


class PaymentMethods(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        verbose_name = "PaymentMethod"
    
    def __str__(self):
        return self.title


class PayoutMethod(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class TimeZone(models.Model):
    zone = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.zone


class SiteSettings(models.Model):
    CURRENCY_CHOICES = (
        ("$", "$"),
        ("???", "???"),
        ("???", "???"),
    )
    CONTACT_LESS_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    MULTI_DELIVERY = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    OTP_CHOICE = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    DELIVERY_FEE_CHOICE = (
        ("Fixed", "Fixed"),
        ("Distance Wise", "Distance Wise")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    site_name = models.CharField(max_length=255, null=True)
    site_logo = models.ImageField(upload_to="images/", null=True, blank=True)
    site_fav_icon = models.ImageField(upload_to="images/", null=True, blank=True)
    support_phone = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, choices=CURRENCY_CHOICES, default="$")
    contact_less_delivery = models.CharField(max_length=255, choices=CONTACT_LESS_CHOICES, default="No")
    store_kilo = models.PositiveIntegerField(null=True, blank=True)
    driver_kilo = models.PositiveIntegerField(null=True, blank=True)
    max_delivery = models.PositiveIntegerField(null=True, blank=True)
    preparation_time = models.PositiveIntegerField(null=True, blank=True)
    multiple_delivery = models.CharField(max_length=255, choices=MULTI_DELIVERY, null=True, blank=True)
    otp_verification = models.CharField(max_length=255, choices=OTP_CHOICE, default="No")
    copyright_year = models.CharField(max_length=255, null=True, blank=True)
    copyright_url = models.CharField(max_length=255, null=True, blank=True)

    # API
    google_api_key = models.CharField(max_length=255, null=True, blank=True)
    google_client_id = models.CharField(max_length=255, null=True, blank=True)
    google_client_secret = models.CharField(max_length=255, null=True, blank=True)
    # Payment 
    payment_methods = models.ManyToManyField(PaymentMethods)
    paypal_access_token = models.CharField(max_length=255, null=True, blank=True)
    paypal_client = models.CharField(max_length=255, null=True, blank=True)
    paypal_secret = models.CharField(max_length=255, null=True, blank=True)
    payout_methods = models.ManyToManyField(PayoutMethod)

    # Email
    driver_email = models.CharField(max_length=255, null=True,blank=True)
    email_host = models.CharField(max_length=255, null=True, blank=True)
    email_port = models.CharField(max_length=255, null=True, blank=True)
    email_from = models.EmailField(null=True, blank=True)
    # Fees
    delivery_fee_type = models.CharField(max_length=255, null=True, blank=True, choices=DELIVERY_FEE_CHOICE)
    delivery_fee = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    booking_fee = models.FloatField(null=True, blank=True)
    store_comission = models.FloatField(null=True, blank=True)
    driver_comission = models.FloatField(null=True, blank=True)

    # usefulllinks
    terms_conditions = models.TextField(null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)
    privacy_policy = models.TextField(null=True, blank=True)

    # Extra fields
    phone_code = models.CharField(max_length=255, null=True, blank=True)
    timezone = models.ForeignKey(TimeZone, on_delete=models.CASCADE, null=True, blank=True)
    schedule_order_time = models.CharField(max_length=255, null=True, blank=True)
    default_rating = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Addons(models.Model):
    STATUS_CHOICE = (
        ("Active", "Active"),
        ("Deactive", "Deactive")
    )

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.id}/"


class Country(models.Model):
    slug = models.SlugField()
    country_name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class City(models.Model):
    slug = models.SlugField()
    city_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.city_name
    
    def get_absolute_url(self):
        return f"/{self.slug}/"