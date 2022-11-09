from django.views import View
from django.shortcuts import render
from .models import Topic, Category, Message, CustomUser, Reply, Receiver
from django.core.handlers.wsgi import WSGIRequest
from .database import Database

class Topics(View):
    def get(self, request: WSGIRequest):
        context = {}
        context['category'] = Category.objects.filter(id=request.GET.get('category')).first()
        context['topics'] = Topic.objects.filter(category_id=context['category'])
        return render(request, 'topics.html', context=context)

class Topic_view(View):
    db = Database()

    def get(self, request: WSGIRequest):
        context = {}
        context['topic'] = Topic.objects.filter(id=request.GET.get('topic')).first()
        context['messages'] =  Message.objects.filter(topic_id=context['topic'])

        if request.user.is_authenticated:
            self.db.read_message(request.user.id, request.GET.get('topic'))

        return render(request, 'topic.html', context=context)

    def post(self, request: WSGIRequest):
        context = {}

        if request.user.is_authenticated:

            if not request.POST.get('reply_to'):
                new_message = Message(
                    text        = request.POST.get('text'),
                    sended_from = CustomUser.objects.get(id = request.user.id),
                    topic       = Topic.objects.get(id=request.POST.get('topic')),
                )
                new_message.save()
            else:
                new_reply = Reply(
                    text        = request.POST.get('text'),
                    sended_from = CustomUser.objects.get(id = request.user.id),
                    reply_to    = Message.objects.get(id=request.POST.get('reply_to')),
                )
                new_reply.save()
                new_sended_to = Receiver(
                    reply   = new_reply,
                    user    = CustomUser.objects.get(id=request.POST.get('sended_to'))
                )
                new_sended_to.save()
            
            self.db.read_message(request.user.id, request.POST.get('topic'))

        context['topic'] = Topic.objects.filter(id=request.POST.get('topic')).first()
        context['messages'] =  Message.objects.filter(topic_id=context['topic'])
        return render(request, 'topic.html', context=context)