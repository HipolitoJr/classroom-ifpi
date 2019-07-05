from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('get_alunos', views.get_alunos, name='get_alunos'),
    path('register', views.register, name='register'),
    path('registered', views.registered, name='registered'),
]