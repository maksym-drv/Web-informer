from django.views import View
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

class Categories(View):

    def get(self, request: WSGIRequest):
        context = {}
        return render(request, 'categories.html', context=context)
