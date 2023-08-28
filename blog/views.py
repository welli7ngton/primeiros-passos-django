from django.http import HttpResponse


# Create your views here.
def blog(request):
    print("Blog")
    return HttpResponse("novo teste de view Blog")


def example(request):
    print("example")
    return HttpResponse("example view")
