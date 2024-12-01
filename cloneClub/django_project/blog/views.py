from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [
    {
        'author': 'jonathan',
        'title': 'My Days are numbered her',
        'pages': 1234,
        'date_created': '1998'
    },
    {
        'author': 'jonathan',
        'title': 'New Beginngs This YeaR',
        'pages': 245,
        'date_created' : '1990'
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
# Create your views here.
