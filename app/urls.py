from django.urls import path
from app.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="HomePageView"),
    # restaurant wise item
    path("restaurant/<str:vendor_name>", RestaurantWiseProduct.as_view(), name="RestaurantWiseItem"),
    # category wise item
    path("category-wise-item/<str:title>/", CategorywiseProduct.as_view(), name="CategoryWiseItem"),
    
    # All Actions
    path("add-to-cart/", add_to_cart, name="addTocart"),
    # checkout
    path("checkout/", checkout, name="checkout")
]
