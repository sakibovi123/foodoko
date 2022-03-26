from django.urls import path
from app.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="HomePageView"),
    # restaurant wise item
    path("restaurant/<str:vendor_name>", RestaurantWiseProduct.as_view(), name="RestaurantWiseItem"),
    # category wise item
    path("category-wise-item/<str:title>/", CategorywiseProduct.as_view(), name="CategoryWiseItem"),

    # User Order page
    path("user-orders/", OrderView.as_view(), name="orderView"),
    # User Order Detail View
    path("<str:invoice_no>/", UserOrderDetail.as_view(), name="UserOrderDetails"),
    
    # All Actions
    path("add-to-cart/", add_to_cart, name="addTocart"),
    # checkout
    path("checkout/", checkout, name="checkout"),
    path("send-money/", send_money, name="send_money"),

    # user settings
    path("user-settings/", UserSettings.as_view(), name="UserSettings"),
]
