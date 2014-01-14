from django.views.generic.base import View
from django.shortcuts import render

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')
