from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username    = None
    email       = models.EmailField(('E-mail address'), unique=True)
    image       = models.ImageField("User photo", null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email