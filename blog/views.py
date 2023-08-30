# from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request):
    print("Blog")
    context = {
        'text': "Titulo Blog",
        'title': 'Blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context=context
    )


def example(request):
    print("Blog")
    context = {
        'text': "Estou no Example",
        'title': "Example",
    }
    return render(
        request,
        'blog/example.html',
        context
    )


def post(request, id):
    print("Post", id)
    context = {
        'text': "Titulo Blog",
        'title': 'Blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context=context
    )