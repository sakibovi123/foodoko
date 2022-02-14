from django.contrib import admin

from vendorside.models import Category, Product
from .models import *
# Register your models here.


admin.site.register([
    Permission,
    Role,
    Driver,
    Category,
    Product
])