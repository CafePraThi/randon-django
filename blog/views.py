from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog.data import posts
from typing import Any
from django.http import HttpRequest
# Create your views here.

def blog(request):
  print('blog')

  context = {
    'texto': 'Bem vindo ao Blog',
    'posts': posts
  }

  return render(request, 'blog/index.html', context)

def post(request: HttpRequest, post_id: int):
  found_post: dict[str, Any] | None = None

  for post in posts:
    if post['id'] == post_id:
      found_post = post
      break

  if found_post is None:
    raise Http404('Post Não existe.')

  context = {
    #'texto': 'Bem vindo ao Blog',
    'post': found_post,
    'title': found_post['title']
    
  }
  return render(request, 'blog/post.html', context)