# Create your views here.
import datetime
import os
import platform
from django.shortcuts import render, render_to_response, redirect
from comum.models import Horario, Turma, MatriculaDisciplinar
from horarios.models import AusenciaInteresse, DeclaracaoAusencia


def get_net_config():
    SO = platform.system()
    arquivo = 'netconf.txt'
    if SO == 'linux':
        os.system("ifconfig > " + arquivo)
    elif SO == 'Windows':
        os.system("ifconfig | " + arquivo)
    return arquivo


def get_ip_wifi():
    ip = ""
    arch = get_net_config()
    text = open(arch)
    lines = text.readlines()
    text.close()
    for l in lines:
        if "inet addr:" in l:
            if "127.0.0.1" not in l:
                ip = l[20:35:]
                print(ip)
    return ip


def home(request):
    ip = get_ip_wifi()
    link = "http://" + ip + ":8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def get_alunos(request):
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
    horario_padrao = Horario.objects.filter(dia_semana=DIAS[hoje.weekday()],
                                            hora_inicio__lte=datetime.datetime.now().time(),
                                            hora_fim__gte=datetime.datetime.now().time())
    horario_vago = DeclaracaoAusencia.objects.filter(horario=horario_padrao[0].id)
    prof_substituto = AusenciaInteresse.objects.filter(ausencia=horario_vago[0].id)
    if prof_substituto.__len__() == 1:
        horario_atual = prof_substituto[0].id
    else:
        horario_atual = horario_padrao[0].id
    turma = Turma.objects.filter(horario=horario_atual)
    turmaDiscId = turma[0].disciplina_id
    matriculas = MatriculaDisciplinar.objects.filter(disciplina=turmaDiscId)
    return render(request, 'qr_code/qr_code_register.html', {'matriculas': matriculas})


def register(request):
    aluno = ''
    if request.method == "POST":
        aluno = request.POST.get("aluno_r")
    response = render_to_response('qr_code/qr_code_registered.html', {'aluno': aluno})
    response.set_cookie('aluno', aluno)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
    else:
        return redirect('get_alunos')
    return render(request, 'qr_code/qr_code_registered.html', {'aluno': aluno})
