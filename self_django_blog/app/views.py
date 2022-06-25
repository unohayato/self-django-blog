from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.


class Index(ListView):
  model = Post
  
class Detail(DetailView):
  model = Post
  
  

 