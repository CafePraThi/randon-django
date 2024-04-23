from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts
# Create your views here.

def blog(request):
  print('blog')

  context = {
    'texto': 'Bem vindo ao Blog',
    'posts': posts
  }

  return render(request, 'blog/index.html', context)