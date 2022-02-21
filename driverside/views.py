from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View


class Driverpanel(View):
    template_name = ""
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)


class Payments(View):
    template_name = ""
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

