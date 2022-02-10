from django.db import models
from django.contrib.auth.models import User


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255, unique=True)
    shop_logo = models.ImageField(upload_to="images/")
    contact_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_sale = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Vendor Profile"

    def __str__(self):
        return self.vendor_name


class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="images/")
    driving_license_photo = models.ImageField(upload_to="images/", null=True, blank=True)
    address = models.CharField(max_length=255)
    total_earning = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total_paid = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "Driver Profile"

    def __str__(self):
        return self.full_name 