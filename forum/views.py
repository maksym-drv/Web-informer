from django.views import View
from django.shortcuts import render
from .models import Topic, Category, Message, CustomUser
from django.core.handlers.wsgi import WSGIRequest

class Topics(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['category'] = Category.objects.filter(id=request.GET.get('category')).first()
        context['topics'] = Topic.objects.filter(category_id=context['category'])
        return render(request, 'topics.html', context=context)

class Topic_view(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['topic'] = Topic.objects.filter(id=request.GET.get('topic')).first()
        context['messages'] =  Message.objects.filter(topic_id=context['topic'])
        return render(request, 'topic.html', context=context)

    def post(self, request: WSGIRequest):
        context = {}

        if request.user.is_authenticated:
            new_comment = Message(
                text        = request.POST.get('text'),
                sended_from = CustomUser.objects.get(id = request.user.id),
                topic       = Topic.objects.get(id=request.POST.get('topic')),
            )
            new_comment.save()

        context['topic'] = Topic.objects.filter(id=request.POST.get('topic')).first()
        context['messages'] =  Message.objects.filter(topic_id=context['topic'])
        return render(request, 'topic.html', context=context)