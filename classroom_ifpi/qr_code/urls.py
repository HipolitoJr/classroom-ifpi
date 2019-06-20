from . import views
from django.urls import path

urlpatterns = [
    path('qr/', views.index, name='index')
]