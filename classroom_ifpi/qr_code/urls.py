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
    path('export', views.export, name='export'),
    path('export_to_csv', views.export_to_csv, name='export_to_csv'),
    path('permission_denied', views.permission_denied, name='permission_denied'),
    path('download_file', views.download_file, name='download_file'),
]
