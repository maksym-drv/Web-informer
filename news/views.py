from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views import View
from . import models

class News(View):

    def get(self, request: WSGIRequest):
        context = {}
        context['news'] = models.News.objects.all()
        context['is_authenticated'] = request.user.is_authenticated
        return render(request, 'news.html', context=context)

class Post(View):

    def get(self, request: WSGIRequest):
        context = {}

        context['post'] = models.News.objects.filter(id = request.GET.get('news-post')).first()
        context['comments'] = models.Comment.objects.filter(news_id = request.GET.get('news-post'))
        context['is_authenticated'] = request.user.is_authenticated
        return render(request, 'news-post.html', context=context)

    def post(self, request: WSGIRequest):
        context = {}

        if request.user.is_authenticated:
            new_comment = models.Comment(
                text        = request.POST.get('text'),
                sended_from = models.CustomUser.objects.get(id = request.user.id),
                news        = models.News.objects.get(id = request.POST.get('news-post')),
            )
            new_comment.save()

        context['post'] = models.News.objects.filter(id = request.POST.get('news-post')).first()
        context['comments'] = models.Comment.objects.filter(news_id = request.POST.get('news-post'))
        context['is_authenticated'] = request.user.is_authenticated
        return render(request, 'news-post.html', context=context)