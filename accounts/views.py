from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# class profile(View):
#     def get(self, request):
#         return render(request, 'weather/index.html')

class Sign_up(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "sign_up.html"