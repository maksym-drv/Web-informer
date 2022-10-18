from django.db import models

class Users(models.Model):
    name        = models.CharField("Name", max_length=200, null=False)
    email       = models.EmailField("E-mail", null=False)
    password    = models.CharField("Password", max_length=500, null=False)
