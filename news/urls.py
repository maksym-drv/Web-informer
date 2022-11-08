from django.urls import path
from .views import News, Post

urlpatterns = [
    path('', News.as_view(), name='news'),
    path('news-post', Post.as_view(), name='post')
]