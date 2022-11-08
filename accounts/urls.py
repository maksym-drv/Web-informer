from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Sign_up, Profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/news/'), name='logout'),
    path('profile/', login_required(Profile.as_view()), name='profile'),
    path('signup/', Sign_up.as_view(), name='signup')
]