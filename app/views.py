from django.shortcuts import render
from django.views import View


class HomePageView(View):
    template_name = "main/index.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)
