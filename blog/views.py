# from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts
from django.http import Http404


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


def post(request, _id):
    print("Post", _id)
    foundPost = None
    for post in posts:
        if post['id'] == _id:
            foundPost = post
            break

    if foundPost is None:
        raise Http404("Pagina não existe")

    context = {
        'post': foundPost,
        'title': foundPost['title'],
    }
    return render(
        request,
        'blog/post.html',
        context=context
    )
