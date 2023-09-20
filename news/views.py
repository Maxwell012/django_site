from django.shortcuts import render
from .models import Articles


def news_home(request):
    data = {
        'news': Articles.objects.all()
    }
    return render(request, 'news/news_home.html', data)


def create(request):
    return render(request, 'news/create.html')
