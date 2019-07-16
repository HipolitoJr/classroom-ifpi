from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('get_alunos', views.get_alunos, name='get_alunos'),
    path('register', views.register, name='register'),
    path('registered', views.registered, name='registered'),
    path('register_expired', views.register_expired, name='register_expired'),
    path('no_has_reg', views.no_has_reg, name='no_has_reg'),
    path('ip_blocked', views.ip_blocked, name='ip_blocked'),
]
