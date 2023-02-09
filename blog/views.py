from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # primeiro argumento é o objeto request, segundo template name que quer carregar, 3° vai passar os dados e permitir utiliza-los na template
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})