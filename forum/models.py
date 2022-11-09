from django.db import models
from accounts.models import CustomUser
from categories.models import Category

class Topic(models.Model):
    title       = models.CharField("Title", max_length=70, null=False)
    description = models.CharField("Pre-text", max_length=300, null=True)
    text        = models.TextField("Full-text", null=False)
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Message(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    topic       = models.ForeignKey(Topic, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Reply(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)
    reply_to    = models.ForeignKey(Message, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name_plural = "Replies"

class Receiver(models.Model):
    reply       = models.OneToOneField(Reply, on_delete = models.CASCADE)
    user        = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    is_read     = models.BooleanField(null=False, default=False)