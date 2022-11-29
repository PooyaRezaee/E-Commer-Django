from django.shortcuts import render
from django.views import View

__all__ = [
    'HomeView',
]

class HomeView(View):
    def get(self,request):
        return render(request,'home/index.html')