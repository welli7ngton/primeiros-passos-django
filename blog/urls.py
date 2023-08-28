from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('example/', views.example),
]
