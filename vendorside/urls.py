from django.urls import path, include
from .views import *


urlpatterns = [
    path("<int:vendor_id>/", VendorPanel.as_view(), name="vendorPanel"),

    # vendor category path
    path("vendor-category/<int:vendor_id>/", CategoryManagement.as_view(), name="vendorCategory"),
    path("create-vendor-category/<int:vendor_id>/", AddCategory.as_view(), name="addCategory"),
    path("edit-category/<int:vendor_id>/<int:cat_id>/", EditCategory.as_view(), name="editCategory"),
    path("delete-category/<int:vendor_id>/<int:cat_id>/", deleteCategory, name="deleteCategory"),

    # vendor product path
    path("vendor-products/<int:vendor_id>/", VendorProductView.as_view(), name="vendorProduct"),
    path("add-vendor-product/<int:vednor_id>/", AddVendorProduct.as_view(), name="addvendorProduct"),
    path("edit-vendor-product/<int:vendor_id>/<int:product_id>/", EditVendorProduct.as_view(), name="editvendorProduct"),
    path("delete-vendor-product/<int:vendor_id>/<int:product_id>/", deleteVendorProduct, name="deletevendorProduct"),

    # All Saled path
    path("all-sales/<int:vendor_id>/", VendorAllSales.as_view(), name="allSales"),
    
    # roles path
    path("role-management/<int:vendor_id>/", RoleManagement.as_view(), name="RoleManagement"),
    path("add-role/<int:vendor_id>/", AddRole.as_view(), name="AddRole"),
    path("edit-role/<int:vendor_id>/", EditRole.as_view(), name="EditRole"),

    # Vendor settings url
    path("vendor-settings/<int:vendor_id>/", VendorSettings.as_view(), name='VendorSettings'),

    # contact admin
    path("contact-admin/<int:vendor_id>/", ContactAdmin.as_view(), name="ContactAdmin"),

    # addons
    path("addons/<int:vendor_id>/", Addons.as_view(), name="Addons"),
]