from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register([
    Coupon,
    Wallet,
    CartItems,
    PaymentMethod,
    Order,
    TransferWalletBalance
])