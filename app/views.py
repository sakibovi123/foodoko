from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.views import View
from vendorside.models import *
from .models import *


class HomePageView(View):
    template_name = "main/index.html"
    def get(self, request):
        all_category = Category.objects.all()
        all_vendors = VendorProfile.objects.all()
        pop_prods = Product.objects.filter(is_popular=True)
        all_prods = Product.objects.all()

        # Wallet
        balance = None
        if request.user.is_authenticated:
            balance = Wallet.objects.get(user=request.user)

        # Cart View
        cart = request.session.get("cart", None)
        if not cart:
            request.session.cart = {}
        cart_products = None
        if cart:
            ids = list(request.session.get("cart").keys())
            cart_products = Product.get_items(ids)
        
        rec_ord_prods = Product.objects.filter(recently_ordered=True)

        restaurants = VendorProfile.objects.all()
        # payment methods
        payment_methods = PaymentMethod.objects.all()
        # all available users
        users = User.objects.exclude(username=request.user)
        args = {
            "all_vendors": all_vendors,
            "pop_prods": pop_prods,
            "all_prods": all_prods,
            "cart_products": cart_products,
            "balance": balance,
            "all_category": all_category,
            "restaurants": restaurants,
            "rec_ord_prods": rec_ord_prods,
            "payment_methods": payment_methods,
            "users": users,
        }
        return render(request, self.template_name, args)


class RestaurantWiseProduct(View):
    template_name = "restaurant/restaurant_wise.html"
    def get(self, request, vendor_name):
        restaurants = get_object_or_404(VendorProfile, vendor_name=vendor_name)
        products = Product.objects.filter(
            vendor__vendor_name=restaurants.vendor_name
        )

        rest_cat = Category.objects.filter(vendor__vendor_name = restaurants.vendor_name)

        args = {
            "restaurants": restaurants,
            "products": products,
            "rest_cat": rest_cat,
        }
        return render(request, self.template_name, args)


class CategorywiseProduct(View):
    template_name = "restaurant/category_wise.html"
    def get(self, request, title):
        cat_obj = get_object_or_404(Category, title=title)
        cat_products = Product.objects.filter(category__title=cat_obj.title)
        args = {
            "cat_obj": cat_obj,
            "cat_products": cat_products,
        }
        return render(request, self.template_name, args)


class SettingsView(View):
    template_name = "main/settings.html"
    def get(self, request, user_id):
        userId = get_object_or_404(User, pk=user_id)
        args = {}
        return render(request, self.template_name, args)

    def post(self, request, user_id):
        userId = get_object_or_404(User, pk=user_id)
        userId.username = request.POST.get("username")
        userId.password = request.POST.get("password")
        userId.first_name = request.POST.get("first_name")
        userId.last_name = request.POST.get("last_name")

        userId.save()
        return redirect("home")


class UserSettings(View):
    template_name = "main/settings.html"

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

class OrderView(View):
    template_name = "restaurant/order.html"

    def get(self, request):
        order = Order.objects.filter(user=request.user)
        args = {
            "order": order,
        }
        return render(request, self.template_name, args)


class UserOrderDetail(View):
    template_name = "restaurant/user_order_details.html"
    def get_object(self, invoice_no):
        try:
            return Order.objects.get(invoice_no=invoice_no)
        except Order.DoesNotExist:
            return Http404

    def get(self, request, invoice_no):
        pass

"""
All Actions
"""
def add_to_cart(request):
    cart = request.session.get("cart")
    remove = request.POST.get("remove")
    product_id = request.POST.get("product_id")

    if product_id is not None:
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session["cart"] = cart
        return redirect("HomePageView")
    else:
        return HttpResponse("Eror 404")


def plusButton(request):
    cart = request.session.get("cart")
    product_id = request.POST.get("product_id")
    if product_id is not None:
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session["cart"] = cart
        return redirect("HomePageView")


def minus_button(request):
    cart = request.session.get("cart")
    minus = request.POST.get("minus")
    product_id = request.POST.get("product_id")

    if product_id is not None:
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if minus:
                    cart[product_id] = quantity - 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session["cart"] = cart
        return redirect(f"/")


def removeCart(request):
    cart = request.session.get("cart", None)
    product_id = request.POST.get("product_id")
    if request.method == "POST":
        if cart:
            cart.pop(product_id)
            request.session["cart"] = cart
            return redirect("cart")
        else:
            return HttpResponse("Backend Error")


def checkout(request):
    if request.method == "POST":
        cart = request.session.get("cart", None)
        ids = list(request.session.get("cart").keys())
        cart_products = Product.get_items(ids)
        user = request.user
        address = request.POST.get("address")
        latitude = request.POST.get("user_lat")
        longtitude = request.POST.get("user_long")
        paymentmethod = request.POST.get("paymentmethod")
        apartment_no = request.POST.get("apartment_no")
        road_no = request.POST.get("road_no")
        flat_no = request.POST.get("flat_no")

        order = Order(
            user=user,
            address=address,
            paymentmethod=PaymentMethod.objects.get(id=paymentmethod),
            latitude=latitude,
            longtitude=longtitude,
            apartment_no=apartment_no,
            road_no=road_no,
            flat_no=flat_no,
        )

        
        total = 0
        for p in cart_products:
            quantity = cart.get(str(p.id))
            total += p.regular_price * quantity
            p.recently_ordered = True
            print(f"VENDORRRRRRR>>>>> {p.vendor}")
            order.vendor = VendorProfile.objects.get(id=p.vendor.id)
            
            p.save()
            cartItems = CartItems(
                product=p,
                quantity=quantity
            )
            cartItems.save()
            order.save()
            order.items.add(cartItems)
        order.total = total
        order.vendor.total_sale += total
        order.vendor.save()
        order.save()
        # clearing session
        cart = {}
        request.session["cart"] = cart
        return redirect(f"HomePageView")


def use_coupon(self, request):
    if request.method == "POST":
        get_coupon = request.POST.get("coupon")
        pass

def pay_with_wallet(self, request, order_id):
    orderId = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        user = request.user
        

def send_money(request):
    user1 = request.user
    post = request.POST
    if request.method == "POST":
        user2 = post["receiver"]
        amount = post["amount"]

        trx = TransferWalletBalance(
            user1=user1,
            user2=User.objects.get(id=user2),
            amount=amount
        )

        trx.save()

        user1.wallet.balance -= trx.amount
        user1.wallet.save()
        trx.user2.wallet.balance += trx.amount
        trx.user2.wallet.save()

        return redirect("HomePageView")