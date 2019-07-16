from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.sites import requests
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone
from django.views.generic.base import View

from comum.models import Turma, Professor
from painel.forms import CadastrarProfessorForm


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

            # if senha != confirma_senha:
            #     return messages.error(request, 'Senhas diferentes!')

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

@login_required
def list_turmas(request):
    turmas = get_turmas(request)
    return render(request,
                  'turmas.html',
                  {'titulo': 'Suas Turmas',
                   'turmas': turmas})


def turma_detalhe(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    return render(request,
                  'turma_detalhe.html',
                  {'titulo': turma.especificacao_disciplina,
                   'turma': turma})


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
