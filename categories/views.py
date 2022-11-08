from django.views import View
from django.shortcuts import render
from .models import Category
from django.core.handlers.wsgi import WSGIRequest

class Categories(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['categories'] = Category.objects.all()
        return render(request, 'categories.html', context=context)