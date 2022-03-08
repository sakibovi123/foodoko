from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from app.models import Order



class Driverpanel(View):
    template_name = "driverpanel/index.html"
    def get(self, request):
        orders = Order.objects.all()
        args = {
            "orders": orders,
        }
        return render(request, self.template_name, args)


class OrderDetailView(View):
    template_name = "driverpanel/order_details.html"
    def get_object(self, order_id):
        try:
            obj = Order.objects.get(pk=order_id)
            return obj
        except Order.DoesNotExist:
            return Http404

    def get(self, request, order_id):
        order_obj = self.get_object(order_id)
        args = {
            "order_obj": order_obj,
        }
        return render(request, self.template_name, args)


class Payments(View):
    template_name = ""
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class DriverSettings(View):
    template_name = ""

    def get(self, request):
        args = {}
        return render(request, self.template_name, args)
