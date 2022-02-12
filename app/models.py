from django.db import models
from django.contrib.auth.models import User
from authentication.models import *
from datetime import date, datetime
from vendorside.models import *


class Coupon(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    discount_amount = models.PositiveIntegerField()
    is_used = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]
        verbose_name = "Coupon"

    def __str__(self):
        return self.code


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return str(self.id)



class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    invoice_no = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    driver = models.ForeignKey(DriverProfile, on_delete=models.DO_NOTHING, null=True, blank=True)

    add_coupon = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Order"

    def __str__(self):
        return self.invoice_no


class FavoriteRestaurants(models.Model):
    created_at = models.DateField(default=date.today)
    restaurant = models.ForeignKey(VendorProfile, on_delete=models.DO_NOTHING)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)



class CancelReason(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.title