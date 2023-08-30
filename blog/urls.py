from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('example/', views.example, name='example'),
]
