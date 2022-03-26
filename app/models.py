from django.db import models
from django.contrib.auth.models import User
from authentication.models import *
from datetime import date, datetime
from vendorside.models import *
import random
import string


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return str(self.id)



class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.product.id}"


class PaymentMethod(models.Model):
    payment_title = models.CharField(max_length=255)

    class Meta:
        ordering = ("payment_title",)

    def __str__(self):
        return f"Payment Title => {self.payment_title}"


class Order(models.Model):
    STATUS_CHOICES = (
        ("Restaurant accepted your order", "Restaurant accepted your order"),
        ("Restaurant is preparing your food", "Restaurant is preparing your food"),
        ("Driver has picked your order", "Driver has picked your order"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
        ("Restaurant rejected your order", "Restaurant rejected your order")
    )
    created_at = models.DateField(default=date.today)
    invoice_no = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longtitude = models.CharField(max_length=255, null=True, blank=True)
    items = models.ManyToManyField(CartItems)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    driver = models.ForeignKey(DriverProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    add_coupon = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, default="Restaurant accepted your order")

    paymentmethod = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True)
    apartment_no = models.CharField(max_length=255, null=True, blank=True)
    road_no = models.CharField(max_length=255, null=True, blank=True)
    flat_no = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Order"

    def __str__(self):
        return str(self.id)
    
    def generate_random_number(self):
        list = []
        for i in range(1,100):
            i = random.randint(1, 10000)
            list.append(i)
        return i

    def save(self, *args, **kwargs):
        self.invoice_no = self.generate_random_number()
        super(Order, self).save(*args, **kwargs)


class FavoriteRestaurants(models.Model):
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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


class TransferWalletBalance(models.Model):
    invoice_no = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.invoice_no
    
    def save(self, *args, **kwargs):
        length = 11
        chars = string.ascii_lowercase
        random_invoice = "".join(random.choice(chars) for i in range(length))
        self.invoice_no = random_invoice
        super(TransferWalletBalance, self).save(*args, **kwargs)