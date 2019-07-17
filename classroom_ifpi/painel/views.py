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

from comum.models import Turma, Professor, Aluno, MatriculaDisciplinar, Curso, Disciplina
from painel.forms import CadastrarProfessorForm, CadastrarAlunoForm, MatricularAlunoForm, CadastrarTurmaForm, \
    CadastrarCursoForm


def painel(request):
    return render(request, 'base.html')


class CadastrarProfessorView(View):

    def get(self, request):
        return render(request, 'cadastro_professor.html')

    def post(self, request):

        form = CadastrarProfessorForm(request.POST)
        if (form.is_valid()):
            dados = form.data
            senha = make_password("%s" % dados['password'])
            confirma_senha = make_password("%s" % dados['confirma_password'])

            if senha != confirma_senha:
                return messages.error(request, 'Senhas diferentes!')

            usuario = User(username=dados['username'],
                           first_name=dados['first_name'],
                           last_name=dados['last_name'],
                           email=dados['email'],
                           password=senha)
            usuario.save()

            professor = Professor(nome="%s %s" % (dados['first_name'], dados['last_name']),
                                  matricula=dados['matricula'],
                                  cpf='123.456.789-09',
                                  usuario_id=usuario.id)

            professor.save()
            # messages.success(request, 'Seu cadastro foi realizado com sucesso.')
            return redirect('/login/')

        messages.error(request, 'Algo deu errado.')
        return render(request, 'cadastro_professor.html', {'form': form})


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

            usuario = User(username='%s' % dados['first_name'],
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

            aluno = Aluno(nome="%s %s" % (dados['first_name'], dados['last_name']),
                          matricula_curso=dados['matricula_curso'],
                          cpf='123.456.789-09',
                          usuario_id=usuario.id,
                          curso_id=dados['curso'])

            aluno.save()
            return redirect('/painel/alunos')

        messages.error(request, 'Algo deu errado.')
        return render(request, 'cadastro_aluno.html', {'form': form})


class MatricularAlunoView(View):

    def get(self, request, turma_id):
        turma = Turma.objects.get(id=turma_id)
        alunos = Aluno.objects.filter(curso=turma.curso)
        return render(request,
                      'cadastro_matricula.html',
                      {'titulo': 'Matricular Aluno',
                       'turma': turma,
                       'alunos': alunos})

    def post(self, request, turma_id):
        form = MatricularAlunoForm(request.POST)
        if (form.is_valid()):
            dados = form.data
            print(dados)
            aluno_id = dados['aluno']
            aluno = Aluno.objects.get(id=aluno_id)
            turma = Turma.objects.get(id=turma_id)

            matricula = MatriculaDisciplinar(matricula=aluno.matricula_curso,
                                             disciplina=turma,
                                             aluno=aluno,
                                             situacao='C')
            matricula.save()

            return redirect('turma_detalhe', turma_id=turma_id)

        return redirect('painel')


class CadastrarCursoView(View):

    def get(self, request):
        return render(request,
                      'cadastro_curso.html',
                      {'titulo': 'Cadastrar Curso'})

    def post(self, request):
        form = CadastrarCursoForm(request.POST)
        if (form.is_valid()):
            dados = form.data

            curso = Curso(descricao=dados['descricao'],
                          tipo=dados['tipo'])
            curso.save()

            return redirect('cursos')

        return redirect('painel')


class CadastrarTurmaView(View):

    def get(self, request):
        professores = Professor.objects.all()
        cursos = Curso.objects.all()
        disciplinas = Disciplina.objects.all()

        return render(request,
                      'cadastro_turma.html',
                      {'titulo': 'Cadastrar Turma',
                       'professores': professores,
                       'cursos': cursos,
                       'disciplinas': disciplinas})

    def post(self, request):
        form = CadastrarTurmaForm(request.POST)
        if (form.is_valid()):
            dados = form.data
            disciplina = Disciplina.objects.get(id=dados['disciplina'])
            professor = Professor.objects.get(id=dados['ministrante'])
            curso = Curso.objects.get(id=dados['curso'])

            turma = Turma(ministrante=professor,
                          especificacao_disciplina=disciplina.descricao,
                          disciplina=disciplina,
                          curso=curso,
                          carga_horaria=dados['carga_horaria'])
            turma.save()

            return redirect('turma_detalhe', turma_id=turma.id)

        return redirect('painel')


# def matricular_aluno(request, turma_id, aluno_id):
#     aluno = Aluno.objects.get(id=aluno_id)
#     turma = Turma.objects.get(id=turma_id)
#     MatriculaDisciplinar.objects.create(matricula=aluno.matricula_curso,
#                                         disciplina=turma.disciplina,
#                                         aluno=aluno,
#                                         situacao='C')

#     return redirect('painel/turmas/', args=(turma_id,))

@login_required
def list_professores(request):
    professores = Professor.objects.all()
    return render(request, 'professores.html',
                  {'titulo': 'Professores cadastrados',
                   'professores': professores})

@login_required
def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html',
                  {'titulo': 'Cursos cadastrados',
                   'cursos': cursos})


@login_required
def list_turmas(request):
    turmas = get_turmas(request)
    return render(request,
                  'turmas.html',
                  {'titulo': 'Suas Turmas',
                   'turmas': turmas})


@login_required
def turma_detalhe(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    alunos = Aluno.objects.all()
    return render(request, 'turma_detalhe.html',
                  {'titulo': turma.especificacao_disciplina,
                   'turma': turma,
                   'alunos': alunos})


@login_required
def list_alunos(request):
    alunos = Aluno.objects.all()

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
        match_check = check_password(password, usuario.password)
        if not match_check:
            messages.error(request, 'Usuário e/ou senha incorretos')

            return redirect('/login')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/painel/')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    return logout_then_login(request, login_url='/login/')
