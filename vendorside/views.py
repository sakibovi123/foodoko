from django.shortcuts import render
from django.views import View
# Create your views here.

class VendorPanel(View):
    template_name = "panel/index.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

