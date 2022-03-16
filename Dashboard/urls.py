from django.urls import path, include
from Dashboard.views import AdminDashboard, CategoryView
from .views import *

urlpatterns = [
    path("", AdminDashboard.as_view(), name="adminDashboard"),
    # Category
    path("category/", CategoryView.as_view(), name="categoryView"),
    path("add-category/", AddCategory.as_view(), name="addCategory"),
    path("delete-category/", deleteCategory, name="deleteCategory"),
    path("edit-category/<int:cat_id>/", EditCategory.as_view(), name="editCategory"),

    # Product Path
    path("products/", ProductView.as_view(), name="productView"),
    path("add-product/", AddProduct.as_view(), name="addProduct"),
    path("delete-product/", deleteProduct, name="deleteProduct"),
    path("edit-product/<int:product_id>/", EditProduct.as_view(), name="editProduct"),

    # Vendor path
    path("vendors/", VendorView.as_view(), name="VendorView"),
    path("add-vendor/", AddVendor.as_view(), name="AddVendor"),
    path("edit-vendor/<int:vendor_id>/", EditVendor.as_view(), name="editVendor"),
    path("delete-vendor/", deleteVendor, name="deleteVendor"),

    # Permission Path
    path("permissions/", PermissionsView.as_view(), name="permissionsView"),
    path("add-permission/", AddPermissions.as_view(), name="addPermission"),
    path("delete-permission/", deletePermission, name="deletePermission"),
    path("edit-permission/<int:p_id>/", EditPermission.as_view(), name="editPermission"),

    # role path
    path("roles/", RoleView.as_view(), name="roleview"),
    path("add-role/", AddRole.as_view(), name="addRole"),
    path("delete-role/", deleteRole, name="roleDelete"),
    path("edit-role/<int:r_id>/", EditRole.as_view(), name="editRole"),

    # Driver path
    path("drivers/", DriverPayoutView.as_view(), name="driverView"),
    path("add-driver/", AddDriver.as_view(), name="addDriver"),
    path("edit-driver/<int:driver_id>/", EditDriver.as_view(), name="editDriver"),
    path("delete-driver/", deleteDriver, name="deleteDriver"),
    path("driver-details/<str:full_name>/", DriverDetailView.as_view(), name="DriverDetailView"),

    # Penalty path
    path("penalty/", PenaltyView.as_view(), name="penaltyview"),
    path("add-penalty/", AddPenalty.as_view(), name="addPenalty"),
    path("edit-penalty/<int:pen_id>/", EditPenalty.as_view(), name="editPenalty"),
    path("delete-penalty/", deletePenalty, name="deletePenalty"),
    

    #vehicles types path
    path("vehicles/", VehicleTypes.as_view(), name="vehicleView"),
    path("add-vehicle/", AddVehicle.as_view(), name="addVehicle"),
    path("edit-vehicle/<int:vehicle_id>/", EditVehicle.as_view(), name="editVehicle"),
    path("delete-vehicle/", delete_vehicle, name="delete_vehicle"),
    # Delete method

    # coupon path
    path("coupons/", Coupons.as_view(), name="coupons"),
    path("add-coupon/", AddCoupon.as_view(), name="addCoupon"),
    path("edit-coupon/<int:coupon_id>/", EditCoupon.as_view(), name="editCoupon"),

    # Settings path
    path("settings/", Settings.as_view(), name="settingsView"),

    # Country path
    path("country-management/", CountryManagement.as_view(), name="CountryManagement"),
    path("add-country/", AddCountry.as_view(), name="AddCountry"),
    path("edit-country/", EditCountry.as_view(), name="EditCountry"),

    # City path
    path("city-management/", CityManagement.as_view(), name="CityManagement"),
    path("add-city/", AddCity.as_view(), name="AddCity"),
    path("edit-city/<slug:city_slug>/", EditCity.as_view(), name="EditCity"),

]