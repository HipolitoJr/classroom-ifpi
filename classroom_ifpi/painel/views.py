from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.sites import requests
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone
from django.views.generic.base import View

from comum.models import Turma, Professor, Aluno, MatriculaDisciplinar, Curso
from painel.forms import CadastrarProfessorForm, CadastrarAlunoForm


def painel(request):
    return render(request, 'base.html')

class CadastrarProfessorView(View):

    def get(self, request):
        return render(request, 'cadastro_professor.html')

    def post(self, request):

        form = CadastrarProfessorForm(request.POST)
        if (form.is_valid()):
            dados = form.data
            senha = make_password("%s" %dados['password'])
            confirma_senha = make_password("%s" %dados['confirma_password'])

            if senha != confirma_senha:
                return messages.error(request, 'Senhas diferentes!')

            usuario = User(username=dados['username'],
                           first_name=dados['first_name'],
                           last_name=dados['last_name'],
                           email=dados['email'],
                           password=senha,
                           last_login=timezone.now(),
                           is_superuser=False,
                           is_staff=True,
                           is_active=True,
                           date_joined=timezone.now())
            usuario.save()

            professor = Professor(nome = "%s %s" %(dados['first_name'], dados['last_name']),
                                  matricula = dados['matricula'],
                                  cpf = '123.456.789-09',
                                  usuario_id = usuario.id)

            professor.save()
            # messages.success(request, 'Seu cadastro foi realizado com sucesso.')
            return redirect('/login/')

        messages.error(request, 'Algo deu errado.')
        return render(request, 'cadastro_professor.html', {'form': form} )


class CadastrarAlunoView(View):

    def get(self, request):
        cursos = Curso.objects.all()
        return render(request,
                      'cadastro_aluno.html',
                      {'titulo': 'Cadastro de Alunos',
                       'cursos': cursos})

    def post(self, request):

        form = CadastrarAlunoForm(request.POST)
        if (form.is_valid()):
            dados = form.data
            senha = make_password("Abcd1234")

            usuario = User(username= '%s'%dados['first_name'],
                           first_name=dados['first_name'],
                           last_name=dados['last_name'],
                           email=dados['email'],
                           password=senha,
                           last_login=timezone.now(),
                           is_superuser=False,
                           is_staff=False,
                           is_active=False,
                           date_joined=timezone.now())
            usuario.save()

            aluno = Aluno(nome = "%s %s" %(dados['first_name'], dados['last_name']),
                          matricula_curso = dados['matricula_curso'],
                          cpf = '123.456.789-09',
                          usuario_id = usuario.id,
                          curso_id = dados['curso'])

            aluno.save()
            # messages.success(request, 'Seu cadastro foi realizado com sucesso.')
            return redirect('/painel/alunos')

        messages.error(request, 'Algo deu errado.')
        return render(request, 'cadastro_aluno.html', {'form': form} )


def list_turmas(request):
    turmas = get_turmas(request)
    return render(request,
                  'turmas.html',
                  {'titulo': 'Suas Turmas',
                   'turmas': turmas})


def list_alunos(request):
    turmas = get_turmas(request)
    alunos = Aluno.objects.all()

    # for turma in turmas:
    #     matricula_disciplinares = MatriculaDisciplinar.objects.filter(turma = turma)
    #     for matricula_disciplinar in matricula_disciplinares:
    #         aluno = Aluno.objects.get(pk=matricula_disciplinar.aluno_id )
    #         alunos.append(aluno)

    return render(request,
                  'alunos.html',
                  {'titulo': 'Seus Alunos',
                   'alunos': alunos})


def get_turmas(request):
    turmas = Turma.objects.filter(ministrante=request.user.professor)
    return turmas


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.get(username=username)
        match_check = check_password(password,usuario.password)
        if not match_check:
            messages.error(request, 'Usuário e/ou senha incorretos')

            return redirect('/login')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('/painel/')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    return logout_then_login(request, login_url='/login/')
