from django.db import models

class Categories(models.Model):
    name = models.CharField("Category's name", max_length=200, null=False)
    description = models.CharField("Category's description", max_length=600, null=True)