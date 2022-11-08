from django.urls import path
from .views import Topics, Topic_view

urlpatterns = [
    path('', Topics.as_view(), name='topics'),
    path('topic', Topic_view.as_view(), name='topic'),
]