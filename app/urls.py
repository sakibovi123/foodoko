from django.urls import path
from app.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="HomePageView"),
    # restaurant wise item
    path("restaurant/", RestaurantWiseProduct.as_view(), name="RestaurantWiseItem"),
    # category wise item
    path("category-wise-item/", CategorywiseProduct.as_view(), name="CategoryWiseItem"),
]
