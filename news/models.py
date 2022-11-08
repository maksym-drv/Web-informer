from django.db import models
from accounts.models import CustomUser
from categories.models import Categories

class News(models.Model):
    title       = models.CharField("Title", max_length=70, null=False)
    pre_text    = models.CharField("Pre-text", max_length=300, null=True)
    full_text   = models.TextField("Full-text", null=False)
    date        = models.DateTimeField("Date/time", auto_now_add=True)
    image       = models.ImageField("Image", null=False)
    category    = models.ForeignKey(Categories, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "News"

class Comment(models.Model):
    text        = models.TextField("Comment text", null=False)
    sended_from = models.ForeignKey(CustomUser , on_delete = models.CASCADE)
    news        = models.ForeignKey(News , on_delete = models.CASCADE)
    time        = models.DateTimeField("Date/time", auto_now_add=True)

    def __str__(self) -> str:
        return self.text