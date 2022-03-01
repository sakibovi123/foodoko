from django.db import models
from django.contrib.auth.models import User
from authentication.models import *
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    category_img = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Category"

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS_CHOICE = (
        ("Active", "Active"),
        ("Deactive", "Deactive")
    )
    STOCK_STATUS = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    title = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    is_out_stock = models.CharField(max_length=255, null=True, blank=True, default="No")
    stock_qty = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    is_popular = models.BooleanField(default=False)
    recently_viewed = models.BooleanField(default=False)

    recently_ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"

    def __str__(self):
        return self.title

    @staticmethod
    def get_items(ids):
        return Product.objects.filter(id__in=ids)
