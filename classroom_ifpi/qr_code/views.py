# Create your views here.
import datetime
import os
import platform
import re
from django.shortcuts import render, render_to_response, redirect
from comum.models import Horario, Turma, MatriculaDisciplinar
from horarios.models import AusenciaInteresse, DeclaracaoAusencia


def get_net_config():
    SO = platform.system()
    arch = 'netconf.txt'
    if SO == 'Linux':
        os.system("ifconfig > " + arch)
    elif SO == 'Windows':
        os.system("rm " + arch)
        os.system("ifconfig | " + arch)
    return arch


def get_ip_wifi():
    ip = "127.0.0.1"
    arch = get_net_config()
    text = open(arch)
    lines = text.readlines()
    text.close()
    for l in lines:
        if "inet addr:" in l:
            if "127.0.0.1" not in l:
                ips = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", l)
                ip = ips[0]
    return ip


def horario_padrao():
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
    horario = Horario.objects.filter(dia_semana=DIAS[hoje.weekday()],
                                     hora_inicio__lte=datetime.datetime.now().time(),
                                     hora_fim__gte=datetime.datetime.now().time())
    return horario[0].id


def turma_alternativa():
    horario_vago = DeclaracaoAusencia.objects.filter(horario=horario_padrao())
    # if horario_vago.__len__() != 0:
    prof_substituto = AusenciaInteresse.objects.filter(ausencia=horario_vago[0].id)
    return prof_substituto


def home(request):
    ip = get_ip_wifi()
    link = "http://" + ip + ":8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def get_alunos(request):
    horario_atual = horario_padrao()
    turma = Turma.objects.filter(horario=horario_atual)
    turmaDiscId = turma[0].disciplina_id
    matriculas = MatriculaDisciplinar.objects.filter(disciplina=turmaDiscId)
    return render(request, 'qr_code/qr_code_register.html', {'matriculas': matriculas})


def register(request):
    aluno = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_cliente = x_forwarded_for.split(',')[0]
    else:
        ip_cliente = request.META.get('REMOTE_ADDR')
    ip_list = []
    if ip_cliente in ip_list:
        print("Voce nao pode responder novamente a chamada")
    else:
        ip_list.append(ip_cliente)
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
