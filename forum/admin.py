from django.contrib import admin
from .models import Topic, Message, Reply

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Reply)