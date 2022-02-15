from itertools import product
from turtle import title
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from authentication.models import VendorProfile
from .models import *
from vendorside.models import Category, Product
# Create your views here.


class AdminDashboard(View):
    template_name = "admin.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        pass


class CategoryView(View):
    template_name = "category/category.html"

    def get(self, request):
        cats = Category.objects.all()
        args = {
            "cats": cats,
        }
        return render(request, self.template_name, args)



class AddCategory(View):
    template_name = "category/add_category.html"

    def get(self, request):
        vendors = VendorProfile.objects.all()
        args = {
            "vendors": vendors,
        }
        return render(request, self.template_name, args)
    
    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            vendor = request.POST.get("vendor")
            category_img = request.FILES.get("category_img")

            Category.objects.create(
                title = title,
                vendor = VendorProfile.objects.get(id=vendor),
                category_img = category_img
            )
            return redirect("categoryView")

# Actions
def deleteCategory(request):
    if request.method == "POST":
        catId = request.POST.get("catId")
        category = Category.objects.get(id=catId)
        category.delete()
        return redirect("categoryView")
    else:
        return HttpResponse("Server Error")


class EditCategory(View):
    template_name = "category/edit_category.html"
    def get(self, request, cat_id):
        catId = get_object_or_404(Category, pk=cat_id)
        vendors = VendorProfile.objects.all()
        args = {
            "catId": catId,
            "vendors": vendors
        }
        return render(request, self.template_name, args)

    def post(self, request, cat_id):
        catId = get_object_or_404(Category, pk=cat_id)
        title = request.POST.get("title")
        vendor = request.POST.get("vendor")
        category_img = request.FILES.get("category_img")


        catId.title = title
        catId.vendor = VendorProfile.objects.get(id=vendor)
        if category_img is not None:
            catId.category_img = category_img
        else:
            catId.category_img = catId.category_img

        catId.save()
        return redirect("categoryView")


class ProductView(View):
    template_name = "product/products.html"

    def get(self, request):
        products = Product.objects.all()
        args = {
            "products": products,
        }
        return render(request, self.template_name, args)


class AddProduct(View):
    template_name = "product/add-product.html"

    def get(self, request):
        category = Category.objects.all()
        vendors = VendorProfile.objects.all()
        args = {
            "category": category,
            "vendors": vendors,
        }
        return render(request, self.template_name, args)

    def post(self ,request):
        if request.method == "POST":
            post = request.POST
            title = post.get("title")
            product_image = request.FILES.get("product_image")
            category = post.get("category")
            vendor = post.get("vendor")
            is_out_stock = post.get("is_out_stock")
            stock_qty = post.get("stock_qty")
            status = post.get("status")
            regular_price = post.get("regular_price")
            sale_price = post.get("sale_price")

            is_popular = post.get("is_popular")
            recently_viewed = post.get("recently_viewed")

            if sale_price != "" and is_popular == "True" and recently_viewed == "True":
                product = Product(
                    title=title,
                    product_image=product_image,
                    category=Category.objects.get(id=category),
                    vendor=VendorProfile.objects.get(id=vendor),
                    is_out_stock=is_out_stock,
                    stock_qty=stock_qty,
                    status=status,
                    regular_price=regular_price,
                    sale_price=sale_price,
                    is_popular=True,
                    recently_viewed=True,
                )
                product.save()
                return redirect()

            else:
                product = Product(
                    title=title,
                    product_image=product_image,
                    category=Category.objects.get(id=category),
                    vendor=VendorProfile.objects.get(id=vendor),
                    is_out_stock=is_out_stock,
                    stock_qty=stock_qty,
                    status=status,
                    regular_price=regular_price,
                    is_popular=False,
                    recently_viewed=False,
                )
                product.save()
                return redirect("productView")


# Delete Method
def deleteProduct(request):
    if request.method == "POST":
        productId = request.POST.get("productId")
        product = Product.objects.get(id=productId)
        product.delete()
        return redirect("productView")



class EditProduct(View):
    template_name = "product/edit-product.html"
    def get(self, request, product_id):
        productId = get_object_or_404(Product, pk=product_id)
        category = Category.objects.all()
        vendors = VendorProfile.objects.all()
        args = {
            "productId": productId,
            "category": category,
            "vendors": vendors,
        }
        return render(request, self.template_name, args)

    def post(self, request, product_id):
        productId = get_object_or_404(Product, pk=product_id)
        title = request.POST.get("title")
        product_image = request.FILES.get("product_image")
        category = request.POST.get("category")
        vendor = request.POST.get("vendor")
        is_out_stock = request.POST.get("is_out_stock")
        stock_qty = request.POST.get("stock_qty")
        status = request.POST.get("status")
        regular_price = request.POST.get("regular_price")
        sale_price = request.POST.get("sale_price")
        is_popular = request.POST.get("is_popular")
        recently_viewed = request.POST.get("recently_viewed")

        productId.title = title

        if product_image is not None:
            productId.product_image = product_image
        else:
            productId.product_image = productId.product_image
        

        productId.category = Category.objects.get(id=category)
        productId.vendor = VendorProfile.objects.get(id=vendor)
        productId.is_out_stock = is_out_stock
        productId.stock_qty = stock_qty
        productId.status = status
        productId.regular_price = regular_price
        productId.sale_price = sale_price
        if is_popular == "True":
            productId.is_popular = True
        else:
            productId.is_popular = False
        if recently_viewed == "True":
            productId.recently_viewed = True
        else:
            productId.recently_viewed = False
        productId.save()
        return redirect("productView")


class PermissionsView(View):
    template_name = "permission/permissions.html"
    def get(self, request):
        permissions = Permission.objects.all()
        args = {
            "permissions": permissions,
        }
        return render(request, self.template_name, args)



class AddPermissions(View):
    template_name = "permission/add_permission.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            permission = Permission(
                title=title
            )
            permission.save()
            return redirect("permissionsView")

# Delete Method
def deletePermission(request):
    if request.method == "POST":
        permission_id = request.POST.get("permission_id")
        if permission_id is not None:
            permission = Permission.objects.get(id=permission_id)
            permission.delete()
            return redirect("permissionsView")
        else:
            return HttpResponse("Field id expected a number but got null value!!")


class EditPermission(View):
    template_name = "permission/edit_permission.html"
    def get(self, request, p_id):
        permissionId = get_object_or_404(Permission, id=p_id)
        args = {
            "permissionId": permissionId,
        }
        return render(request, self.template_name, args)

    def post(self, request, p_id):
        permissionId = get_object_or_404(Permission, pk=p_id)
        title = request.POST.get("title")
        if request.method == "POST":
            if title != "":
                permissionId.title = title
                permissionId.save()
                return redirect("permissionsView")
            else:
                return redirect("Title is empty")
        else:
            return HttpResponse("method not found")


class RoleView(View):
    template_name = "roles/roles.html"
    def get(self, request):
        roles = Role.objects.all()
        args = {
            "roles": roles,
        }
        return render(request, self.template_name, args)

# delete method
def deleteRole(request):
    if request.method == "POST":
        role_id = request.POST.get("role_id")
        roleId = get_object_or_404(Role, id=role_id)
        roleId.delete()
        return redirect("roleview")
    else:
        return HttpResponse("Server Error")


class AddRole(View):
    template_name = "roles/add_role.html"
    def get(self, request):
        permissions = Permission.objects.all()
        args = {
            "permissions": permissions,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        role_title = request.POST.get("role_title")
        ids = [x.title for x in Permission.objects.all()]
        permission_ids = []
        for x in ids:
            permission_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print(f"Erroor=>Error")
        role = Role.objects.create(
            role_title=role_title
        )
        for x in permission_ids:
            role.permissions.add(Permission.objects.get(id=x))
        return redirect("roleview")


class EditRole(View):
    template_name = "roles/edit_roles.html"
    def get(self, request, r_id):
        roleId = get_object_or_404(Role, pk=r_id)
        permissions = Permission.objects.all()
        args = {
            "roleId": roleId,
            "permissions": permissions,
        }
        return render(request, self.template_name, args)

    def post(self, request, r_id):
        roleId = get_object_or_404(Role, pk=r_id)
        role_title = request.POST.get("role_title")

        roleId.role_title = role_title
        ids = [x.title for x in Permission.objects.all()]
        permission_ids = []
        for x in ids:
            permission_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print(f"Erroor=>Error")
        roleId.title = role_title
        for x in permission_ids:
            roleId.permissions.add(Permission.objects.get(id=x))

        roleId.save()
        return redirect("roleview")



class StorePayoutView(View):
    template_name = "store/payout.html"

    def get(self, request):
        stores = VendorProfile.objects.all()
        args = {
            "stores": stores,
        }
        return render(request, self.template_name, args)


class DriverPayoutView(View):
    template_name = "store/driver_payout.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class AddDriver(View):
    template_name = "store/add_driver.html"
    
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class EditDriver(View):
    template_name = "store/edit_driver.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        pass


def deleteDriver(request, d_id):
    driverId = get_object_or_404(DriverProfile, pk=d_id)
    driverId.delete()
    return redirect()


class Penalty(View):
    template_name = "penalty/penalty.html"
    
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class AddPenalty(View):
    template_name = "penalty/add_penalty.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            driver = request.POST.get("driver")
            status = request.POST.get("status")

            penalty = Penalty(
                driver = DriverProfile.objects.get(id=driver),
                status = status
            )
            penalty.save()
            return redirect("")


class EditPenalty(View):
    template_name = "penalty/edit_penalty.html"
    def get(self, request, pen_id):
        penId = Penalty.objects.get(pk=pen_id)
        args = {
            "penId": penId,
        }
        return render(request, self.template_name, args)
    
    def post(self, request, pen_id):
        penId = Penalty.objects.get(pk=pen_id)
        driver = request.POST.get("driver")
        status = request.POST.get("status")

        penId.driver = DriverProfile.objects.get(id=driver)
        penId.status = status

        penId.save()

        return redirect()


# Delete Method
def deletePenalty(request, pen_id):
    penId = get_object_or_404(Penalty, id=pen_id)
    penId.delete()
    return redirect("")


class VendorView(View):
    template_name = "vendor/vendors.html"

    def get(self, request):
        vendors = VendorProfile.objects.all()
        args = {
            "vendors": vendors,
        }
        return render(request, self.template_name, args)


class AddVendor(View):
    template_name = "vendor/add_vendor.html"

    def get(self, request):
        users = User.objects.all()
        args = {
            "users": users,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            user = request.POST.get("user")
            vendor_name = request.POST.get("vendor_name")
            shop_name = request.POST.get("shop_name")
            shop_logo = request.FILES.get("uploadImg")
            contact_number = request.POST.get("contact_number")
            address = request.POST.get("address")

            if user is not None:
                VendorProfile.objects.create(
                    user=User.objects.get(id=user),
                    vendor_name=vendor_name,
                    shop_logo=shop_logo,
                    shop_name=shop_name,
                    contact_number=contact_number,
                    address=address
                )
                return redirect("VendorView")
            else:
                return HttpResponse("something Went Wrong")


class EditVendor(View):
    template_name = "vendor/edit_vendor.html"

    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, id=vendor_id)
        args = {
            "vendorId": vendorId,
        }
        return render(request, self.template_name, args)

    def post(self, request, vendor_id):
        pass

def deleteVendor(request):
    if request.method == "POST":
        vendor_id = request.POST.get("vendor_id")
        vendorId = get_object_or_404(VendorProfile, id=vendor_id)
        vendorId.delete()
        return redirect("VendorView")
    else:
        return HttpResponse("Server Error")



class VehicleTypes(View):
    template_name = "vehicles/vehicles.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class AddVehicle(View):
    template_name = "vehicles/add_vehicle.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class EditVehicle(View):
    template_name = "vehicles/edit_vehicle.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class Coupons(View):
    template_name = "coupons/coupons.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class AddCoupon(View):
    template_name = "coupons/add_coupon.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class EditCoupon(View):
    template_name = "coupons/edit_coupon.html"

    def get(self, request, coupon_id):
        args = {}
        return render(request, self.template_name, args)


class Settings(View):
    template_name = "settings/settings.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)
        