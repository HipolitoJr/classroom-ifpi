# Create your views here.
import datetime

from django.shortcuts import render, render_to_response, redirect
from comum.models import Aluno, Horario, Turma, MatriculaDisciplinar


def home(request):
    link = "http://192.168.43.174:8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def getAlunos(request):
    DIAS = (
        'SEGUNDA',
        'TERCA',
        'QUARTA',
        'QUINTA',
        'SEXTA',
        'SABADO',
        'DOMINGO',
    )
    hoje = datetime.date.today()
    hoje_dia = hoje.weekday()
    hoje_dia_semana = DIAS[hoje_dia]
    horario_atual = Horario.objects.filter(dia_semana=hoje_dia_semana, hora_inicio__lte=datetime.datetime.now().time(),
                                           hora_fim__gte=datetime.datetime.now().time())
    horario_a = horario_atual[0].id
    turma = Turma.objects.filter(horario=horario_a)
    turmaDiscId = turma[0].disciplina_id
    matriculas = MatriculaDisciplinar.objects.filter(disciplina=turmaDiscId)
    return render(request, 'qr_code/qr_code_register.html', {'matriculas': matriculas})


def register(request):
    aluno = ''
    if request.method == "POST":
        aluno = request.POST.get("aluno_r")
    response = render_to_response('qr_code/qr_code_registered.html', {})
    response.set_cookie('aluno', aluno)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
    else:
        return redirect('getAlunos')
    return render(request, 'qr_code/qr_code_registered.html', {})
