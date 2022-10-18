from django.db import models
from accounts.models import Users
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
    sended_from = models.ForeignKey(Users , on_delete = models.CASCADE)
    topic       = models.ForeignKey(Topics , on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)

class Replies(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(Users , on_delete = models.CASCADE)
    topic       = models.ForeignKey(Topics , on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)
    reply_to    = models.ForeignKey(Messages , on_delete = models.CASCADE)