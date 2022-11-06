from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class TstClass(View):
    def get(self, request):
        return render(request, 'weather/index.html')
        #return HttpResponse({'hello': 'world'})