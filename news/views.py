from django.shortcuts import render
from django.views import View
from . import models

class News(View):

    def get(self, request):
        context = {}
        context['news'] = models.News.objects.all()
        return render(request, 'news.html', context=context)
        