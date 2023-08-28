# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def blog(request):
    print("Blog")
    return render(
        request,
        'blog/index.html'
    )


def example(request):
    print("Blog")
    return render(
        request,
        'blog/example.html'
    )
