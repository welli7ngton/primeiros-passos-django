from django.shortcuts import render


# Create your views here.
def home(request):
    print("Home")

    context = {
        'text': "Estou na Home",
        'title': "Home",
    }

    return render(
        request,
        'home/index.html',
        context
    )
