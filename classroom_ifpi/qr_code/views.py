# Create your views here.
import datetime

from django.shortcuts import render, render_to_response, redirect
from comum.models import Aluno, Horario, Turma, MatriculaDisciplinar
from qr_code.forms import MatriculaDisciplinarForm


def home(request):
    link = "http://192.168.43.174:8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def register(request):
    form = MatriculaDisciplinarForm()
    aluno = ''
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
    response = render_to_response('qr_code/qr_code_register.html', {'matriculas': matriculas})
    # response = render_to_response('qr_code/qr_code_register.html', {'form': form})
    response.set_cookie('aluno', aluno)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
    else:
        return redirect('register')
    return render(request, 'qr_code/qr_code_registered.html', {})
