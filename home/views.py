from django.http import HttpResponse


# Create your views here.
def home(request):
    print("Home")
    return HttpResponse("Novo teste de view Home")
