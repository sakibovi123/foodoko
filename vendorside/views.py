from lib2to3.refactor import get_all_fix_names
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from authentication.models import VendorProfile

from vendorside.models import Category, Product



class VendorPanel(View):
    template_name = "panel/index.html"
    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        args = {
            "vendorId": vendorId,
        }
        return render(request, self.template_name, args)



class CategoryManagement(View):
    template_name = "panel/categoryManagement/vendor_category.html"
    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        cats = Category.objects.filter(vendor=vendorId)
        args = {
            "vendorId": vendorId,
            "cats": cats,
        }
        return render(request, self.template_name, args)



class AddCategory(View):
    template_name = "panel/categoryManagement/add_category.html"
    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if vendorId.user != request.user:
            return HttpResponse("Error")
        else:
            args = {
                "vendorId": vendorId,
            }
            return render(request, self.template_name, args)

    def post(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if request.method == "POST":
            title = request.POST.get("title")
            vendor = request.POST.get("vendor")
            category_img = request.FILES.get("category_img")

            if title != "" and vendor != "" and category_img != "":
                Category.objects.create(
                    title=title,
                    vendor=vendorId.id,
                    category_img=category_img
                )
                return redirect("")
        else:
            return HttpResponse("Server Error")



class EditCategory(View):
    template_name = "panel/categoryManagement/edit_category.html"
    def get(self, request, vendor_id, cat_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        catId = get_object_or_404(Category, id=cat_id)
        if vendorId.user == request.user:
            args = {
                "vendorId": vendorId,
                "catId": catId,
            }
            return render(request, self.template_name, args)
        else:
            return HttpResponse("Error")

    def post(self, request, vendor_id, cat_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        catId = get_object_or_404(Category, id=cat_id)
        if vendorId.user == request.user:
            if request.method == "POST":
                title = request.POST.get("title")
                vendor = VendorProfile.objects.get(id=vendorId.id)
                category_img = request.FILES.get("category_img")

                catId.title = title
                catId.vendor = vendor
                catId.category_img = category_img

                catId.save()
                return redirect()
            else:
                return HttpResponse("error")

        else:
            return HttpResponse("Error")


# Delete Category Method
def deleteCategory(request, vendor_id, cat_id):
    vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
    catId = get_object_or_404(Category, id=cat_id)
    catId.delete()
    return redirect("")



class VendorProductView(View):
    template_name = "panel/productManagement/products.html"

    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if vendorId.user == request.user:
            args = {
                "vendorId": vendorId,
            }
            return render(request, self.template_name, args)
        else:
            return HttpResponse("You are not the owner")


class AddVendorProduct(View):
    template_name = "panel/productManagement/add_product.html"

    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if vendorId.user == request.user:
            args = {}
            return render(request, self.template_name, args)

    def post(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if request.method == "POST":
            title = request.POST.get("title")
            product_image = request.POST.get("product_image")
            category = request.POST.get("category")
            vendor = vendorId.id
            is_out_stock = request.POST.get("is_out_stock")
            status = request.POST.get("status")
            regular_price = request.POST.get("regular_price")
            sale_price = request.POST.get("sale_price")

            is_popular = request.POST.get("is_popular")

            if sale_price != "" and is_popular == True:
                product = Product(
                    title=title,
                    product_image=product_image,
                    category=Category.objects.get(id=category),
                    vendor=vendor,
                    is_out_stock=is_out_stock,
                    status=status,
                    regular_price=regular_price,
                    is_popular=True,
                    recently_viewed=False,
                )
                product.save()
                return redirect("")
            else:
                product = Product(
                    title=title,
                    product_image=product_image,
                    category=Category.objects.get(id=category),
                    vendor=vendor,
                    is_out_stock=is_out_stock,
                    status=status,
                    regular_price=regular_price,
                    sale_price=sale_price,
                    is_popular=False,
                    recently_viewed=False,
                )
                product.save()
                return redirect("")

    

class EditVendorProduct(View):
    template_name = "panel/productManagement/edit_product.html"

    def get(self ,request, vendor_id, product_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        productId = get_object_or_404(Product, pk=product_id)

        if vendorId.user == request.user:
            args = {}
            return render(request, self.template_name, args)
        else:
            return HttpResponse("ERROR")

    def post(self, request, vendor_id, product_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        if vendorId.user == request.user:
            productId = get_object_or_404(Product, pk=product_id)
            if productId is not None:
                title = request.POST.get("title")
                product_image = request.FILES.get("product_image")
                category = request.POST.get("category")
                vendor = vendorId.id
                is_out_stock = request.POST.get("is_out_stock")
                status = request.POST.get("status")
                regular_price = request.POST.get("regular_price")
                sale_price = request.POST.get("sale_price")

                is_popular = request.POST.get("is_popular")

                if sale_price != "" and is_popular == True:
                    productId.title = title
                    productId.product_image = product_image
                    productId.category = Category.objects.get(id=category)
                    productId.vendor = vendor
                    productId.is_out_stock = is_out_stock
                    productId.status = status
                    productId.regular_price = regular_price
                    productId.is_popular = True
                    productId.recently_viewed = False

                    productId.save()
                    return redirect()
                else:
                    productId.title = title
                    productId.product_image = product_image
                    productId.category = Category.objects.get(id=category)
                    productId.vendor = vendor
                    productId.is_out_stock = is_out_stock
                    productId.status = status
                    productId.regular_price = regular_price
                    productId.sale_price = sale_price
                    productId.is_popular = False
                    productId.recently_viewed = False

                    productId.save()
                    return redirect()


    
def deleteVendorProduct(request, vendor_id, product_id):
    vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
    productId = get_object_or_404(Product, id=vendorId)
    if request.method == "POST":
        productId.delete()
        return redirect("")
    else:
        return HttpResponse("Error 404")


class VendorAllSales(View):
    template_name = "panel/allSales/all_sale.html"

    def get(self, request, vendor_id):
        vendorId = get_object_or_404(VendorProfile, pk=vendor_id)
        args = {
            "vendorId": vendorId,
        }
        return render(request, self.template_name, args)




    


