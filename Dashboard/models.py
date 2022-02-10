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