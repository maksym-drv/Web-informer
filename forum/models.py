from django.db import models
from accounts.models import CustomUser
from categories.models import Categories

class Topic(models.Model):
    title       = models.CharField("Title", max_length=70, null=False)
    description = models.CharField("Pre-text", max_length=300, null=True)
    text        = models.TextField("Full-text", null=False)
    date        = models.DateField("Date", auto_now_add=True)
    image       = models.ImageField("Image", null=False)
    category    = models.ForeignKey(Categories, on_delete = models.CASCADE)

class Message(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    topic       = models.ForeignKey(Topic, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)

class Reply(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)
    reply_to    = models.ForeignKey(Message, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name_plural = "Replies"

class Sended_to(models.Model):
    reply   = models.OneToOneField(Reply, on_delete = models.CASCADE)
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    is_read         = models.BooleanField(null=False, default=False)