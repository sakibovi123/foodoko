from django.urls import path, include
from .views import *


urlpatterns = [
    path("", VendorPanel.as_view(), name="vendorPanel"),
]