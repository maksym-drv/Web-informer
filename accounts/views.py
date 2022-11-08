from .forms import SignUpForm
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.handlers.wsgi import WSGIRequest

class Profile(View):

    def get(self, request: WSGIRequest):
        context = {}
        context['form'] = SignUpForm(instance=request.user)

        return render(request, 'profile.html', context=context)

class Sign_up(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "sign_up.html"