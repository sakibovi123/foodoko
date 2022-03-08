from django.urls import path, include
from driverside.views import *

urlpatterns = [
    path("", Driverpanel.as_view(), name='Driverpanel'),
    path("order-details/<int:order_id>/", OrderDetailView.as_view(), name="OrderDetailView"),
    path("driver-settings/", DriverSettings.as_view(), name="driverSettings"),
]
