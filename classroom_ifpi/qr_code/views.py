# Create your views here.
import datetime

from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from comum.models import Aluno, Horario, Turma
from frequencia.models import Frequencia

def home(request):
    link = "http://192.168.43.174:8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def register(request):
    DIAS= (
        ('SEGUNDA'),
        ('TERCA' ),
        ('QUARTA'),
        ('QUINTA'),
        ('SEXTA'),
        ('SABADO'),
        ('DOMINGO'),
    )
    hoje = datetime.date.today()
    hoje_dia = hoje.weekday()
    hoje_dia_semana = DIAS[hoje_dia]
    aluno = ''
    horarios = Horario.objects.filter(dia_semana=hoje_dia_semana)
    alunos = horarios.get(Aluno.objects.all())
    response = render_to_response('qr_code/qr_code_register.html', {'alunos': alunos})
    response.set_cookie('aluno', aluno)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
    else:
        return redirect('register')
    return render(request, 'qr_code/qr_code_registered.html', {})
