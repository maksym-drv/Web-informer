from django.contrib import admin
from .models import CustomUser


class PostCodesAdmin(admin.ModelAdmin):
    exclude = ('password',)

admin.site.register(CustomUser, PostCodesAdmin)