"""classroom_ifpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from comum.views import *
from frequencia.views import *
from horarios.views import *
from rest_framework import routers
from comum import views as comum_views
from horarios import views as horario_views
from frequencia import views as frequencia_views
from painel import views as painel_views
from qr_code import views


# router = routers.DefaultRouter()
# router.register(r'aluno', AlunoDetail, base_name="alunos")
# # router.register(r'professor', ProfessorDetail, base_name="professores")
# router.register(r'disciplina', DisciplinaDetail, base_name="disciplinas")
# router.register(r'curso', CursoDetail, base_name="cursos")
# router.register(r'turma', TurmaDetail, base_name="turmas")
# router.register(r'matriculaDisciplinar', MatriculaDisciplinarDetail, base_name="matriculaDisciplinares")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('qr/', include('qr_code.urls')),
    # path('', include(router.urls)),

    #URLs API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', comum_views.ApiRoot.as_view(), name=comum_views.ApiRoot.name),
    path('api/professores/<int:pk>', comum_views.ProfessorDetail.as_view(), name =comum_views.ProfessorDetail.name ),
    path('api/professores/', comum_views.ProfessorList.as_view(), name = comum_views.ProfessorList.name),
    path('api/usuarios/<int:pk>', comum_views.UserDetail.as_view(), name = comum_views.UserDetail.name),
    path('api/usuarios/', comum_views.UserList.as_view(), name = comum_views.UserList.name),
    path('api/alunos/<int:pk>', comum_views.AlunoDetail.as_view(), name = comum_views.AlunoDetail.name),
    path('api/alunos/', comum_views.AlunoList.as_view(), name = comum_views.AlunoList.name),
    path('api/cursos/<int:pk>', comum_views.CursoDetail.as_view(), name=comum_views.CursoDetail.name),
    path('api/cursos/', comum_views.CursoList.as_view(), name=comum_views.CursoList.name),
    path('api/disciplinas/<int:pk>', comum_views.DisciplinaDetail.as_view(), name=comum_views.DisciplinaDetail.name),
    path('api/disciplinas/', comum_views.DisciplinaList.as_view(), name=comum_views.DisciplinaList.name),
    path('api/turmas/<int:pk>', comum_views.TurmaDetail.as_view(), name=comum_views.TurmaDetail.name),
    path('api/turmas/', comum_views.TurmaList.as_view(), name=comum_views.TurmaList.name),
    path('api/matriculas/<int:pk>', comum_views.MatriculaDisciplinarDetail.as_view(), name=comum_views.MatriculaDisciplinarDetail.name),
    path('api/matriculas/', comum_views.MatriculaDisciplinarList.as_view(), name=comum_views.MatriculaDisciplinarList.name),
    path('api/horarios/<int:pk>', comum_views.HorarioDetail.as_view(), name=comum_views.HorarioDetail.name),
    path('api/horarios/', comum_views.HorarioList.as_view(), name = comum_views.HorarioList.name),
    path('api/declaracoes-ausencias/<int:pk>/', horario_views.DeclaracaoAusenciaDetail.as_view(), name=horario_views.DeclaracaoAusenciaDetail.name),
    path('api/declaracoes-ausencias/', horario_views.DeclaracaoAusenciaList.as_view(), name = horario_views.DeclaracaoAusenciaList.name),
    path('api/declaracoes-interesses/<int:pk>', horario_views.DeclaracaoInteresseDetail.as_view(), name=horario_views.DeclaracaoInteresseDetail.name),
    path('api/declaracoes-interesses/', horario_views.DeclaracaoInteresseList.as_view(), name=horario_views.DeclaracaoInteresseList.name),
    path('api/ausencias-interesses/<int:pk>', horario_views.AusenciaInteresseDetail.as_view(), name=horario_views.AusenciaInteresseDetail.name),
    path('api/ausencias-interesses/', horario_views.AusenciaInteresseList.as_view(), name=horario_views.AusenciaInteresseList.name),
    path('api/frequencias/<int:pk>', frequencia_views.FrequenciaDetail.as_view(), name=frequencia_views.FrequenciaDetail.name),
    path('api/frequencias/', frequencia_views.FrequenciaList.as_view(), name = frequencia_views.FrequenciaList.name),
    path('api/registros/<int:pk>', frequencia_views.RegistroDetail.as_view(), name=frequencia_views.RegistroDetail.name),
    path('api/registros/', frequencia_views.RegistroList.as_view(), name = frequencia_views.RegistroList.name),

    path('painel/', painel_views.painel, name = 'painel'),
]
