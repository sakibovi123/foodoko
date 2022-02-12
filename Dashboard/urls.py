from django.urls import path, include
from Dashboard.views import AdminDashboard, CategoryView
from .views import *

urlpatterns = [
    path("", AdminDashboard.as_view(), name="adminDashboard"),
    # Category
    path("category/", CategoryView.as_view(), name="categoryView"),
    path("add-category/", AddCategory.as_view(), name="addCategory"),
    path("delete-category/<int:cat_id>/", deleteCategory, name="deleteCategory"),
    path("edit-category/<int:cat_id>/", EditCategory.as_view(), name="editCategory"),

    # Product Path
    path("products/", ProductView.as_view(), name="productView"),
    path("add-product/", AddProduct.as_view(), name="addProduct"),
    path("delete-product/", deleteProduct, name="deleteProduct"),
    path("edit-product/<int:product_id>/", EditProduct.as_view(), name="editProduct"),

    # Vendor path
    path("vendors/", VendorView.as_view(), name="VendorView"),
    path("add-vendor/", AddVendor.as_view(), name="AddVendor"),
    path("edit-vendor/", EditVendor.as_view(), name="editVendor"),
    path("delete-vendor/", deleteVendor, name="deleteVendor"),

    # Permission Path
    path("permissions/", PermissionsView.as_view(), name="permissionsView"),
    path("add-permission/", AddPermissions.as_view(), name="addPermission"),
    path("delete-permission/<int:p_id>", deletePermission, name="deletePermission"),
    path("edit-permission/<int:p_id>/", EditPermission.as_view(), name="editPermission"),

    # role path
    path("roles/", RoleView.as_view(), name="roleview"),
    path("add-role/", AddRole.as_view(), name="addRole"),
    path("delete-role/<int:r_id>/", deleteRole, name="roleDelete"),
    path("edit-role/<int:r_id>/", EditRole.as_view(), name="editRole"),

    # Driver path
    path("drivers/", DriverPayoutView.as_view(), name="driverView"),
    path("add-driver/", AddDriver.as_view(), name="addDriver"),
    path("edit-driver/", EditDriver.as_view(), name="editDriver"),
    path("delete-driver/", deleteDriver, name="deleteDriver"),

    # Penalty path
    path("penalty/", Penalty.as_view(), name="penaltyview"),
    path("add-penalty/", AddPenalty.as_view(), name="addPenalty"),
    path("edit-penalty/<int:pen_id>/", EditPenalty.as_view(), name="editPenalty"),
    path("delete-penalty/", deletePenalty, name="deletePenalty"),

    #vehicles types path
    path("vehicles/", VehicleTypes.as_view(), name="vehicleView"),
    path("add-vehicle/", AddVehicle.as_view(), name="addVehicle"),
    path("edit-vehicle/", EditVehicle.as_view(), name="editVehicle"),
    # Delete method

    # coupon path
    path("coupons/", Coupons.as_view(), name="coupons"),
    path("add-coupon/", AddCoupon.as_view(), name="addCoupon"),
    path("edit-coupon/<int:coupon_id>/", EditCoupon.as_view(), name="editCoupon"),

]