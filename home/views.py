from django.shortcuts import render
# Create your views here.

def home(request):
  print('home')

  context={'text': 'asdasd',
           'title': 'Home',
           }

  return render(request, 'home/index.html', context)