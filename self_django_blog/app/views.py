from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexView(View):
  template_name = 'app/index.html'
  
  def get(self, request, *args, **kwargs):
    return render(request, 'app/index.html', )