from email.policy import default
from enum import unique
from django.db import models
from accounts.models import CustomUser
from categories.models import Categories

class Topics(models.Model):
    title       = models.CharField("Title", max_length=70, null=False)
    description = models.CharField("Pre-text", max_length=300, null=True)
    text        = models.TextField("Full-text", null=False)
    date        = models.DateField("Date", auto_now_add=True)
    image       = models.ImageField("Image", null=False)
    category    = models.ForeignKey(Categories, on_delete = models.CASCADE)

class Messages(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    topic       = models.ForeignKey(Topics, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)

class Replies(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)
    reply_to    = models.ForeignKey(Messages, on_delete = models.CASCADE)

class Sended_to(models.Model):
    message_reply   = models.ForeignKey(Replies, on_delete = models.CASCADE)
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    is_read         = models.BooleanField(null=False, default=False)