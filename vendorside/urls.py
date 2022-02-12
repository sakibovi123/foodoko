from django.urls import path, include
from .views import *


urlpatterns = [
    path("<int:vendor_id>/", VendorPanel.as_view(), name="vendorPanel"),

    # vendor category path
    path("vendor-category/<int:vendor_id>/", CategoryManagement.as_view(), name="vendorCategory"),
    path("create-vendor/<int:vendor_id>/", AddCategory.as_view(), name="addCategory"),
    path("edit-category/<int:vendor_id>/<int:cat_id>/", EditCategory.as_view(), name="editCategory"),
    path("delete-category/<int:vendor_id>/<int:cat_id>/", deleteCategory, name="deleteCategory"),
]