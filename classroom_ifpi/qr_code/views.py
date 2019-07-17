# Create your views here.
import datetime
import os
import platform
import re
from django.shortcuts import render, render_to_response, redirect
from comum.models import Horario, MatriculaDisciplinar
from frequencia.models import Registro, Frequencia
from qr_code.models import IPAdress


def get_net_config():
    SO = platform.system()
    arch = 'netconf.txt'
    if SO == 'Linux':
        os.system("ifconfig > " + arch)
    elif SO == 'Windows':
        os.system("ipconfig | " + arch)
    return arch


def get_ip_wifi():
    os.system("rm netconf.txt")
    arq = open("netconf.txt", 'w')
    arq.close()
    arch = get_net_config()
    text = open(arch)
    lines = text.readlines()
    text.close()
    if platform.system() == 'Linux':
        ip = read_linux(lines)
    elif platform.system() == 'Windows':
        ip = read_windows(lines)
    else:
        ip = "127.0.0.1"
    return ip


def read_linux(lines):
    ip = ""
    for l in range(len(lines)):
        if "wlp8s0" in lines[l]:
            lines[l] = lines[l + 1]
            if "inet addr:" in lines[l]:
                if "127.0.0.1" not in lines[l]:
                    ips = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", lines[l])
                    ip = ips[0]
    return ip


def read_windows(lines):
    ip = ""
    for l in range(len(lines)):
        if "Adaptador de Rede sem Fio Wi-Fi:" in lines[l]:
            lines[l] = lines[l + 4]
            if "IPv4" in lines[l]:
                ips = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", lines[l])
                ip = ips[0]
    return ip


def horario_normal():
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
    return horario[0]


def home(request):
    ip = get_ip_wifi()
    link = "http://" + ip + ":8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def get_freq():
    try:
        freq = Frequencia.objects.filter(data=datetime.date.today(),
                                         hora_inicio__lte=datetime.datetime.now().time(),
                                         hora_fim__gte=datetime.datetime.now().time())
        return freq[0]
    except IndexError:
        return redirect('no_has_reg')


def get_alunos(request):
    freq = get_freq()
    matriculas = freq.disciplina.matricula_disciplinar.all()
    return render(request, 'qr_code/qr_code_register.html', {'matriculas': matriculas})


def ip_blocked(request):
    return render(request, 'qr_code/qr_code_ip_blocked.html')


def aluno_registered(matricula):
    reg = False
    freq = get_freq()
    registros = Registro.objects.filter(frequencia=freq.id)
    for r in registros:
        if r.aluno == matricula:
            return True
    return reg


def ip_repetido(request, matricula):
    rep = False
    freq = get_freq()
    reg_ip = IPAdress.objects.filter(frequencia=freq)
    IP = IPAdress()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_cliente = x_forwarded_for.split(',')[0]
    else:
        ip_cliente = request.META.get('REMOTE_ADDR')
    for i in reg_ip:
        if i.ip == ip_cliente:
            rep = True
    if rep is False:
        IP.ip = ip_cliente
        IP.frequencia = freq
        IP.matricula_disciplinar = matricula
        IP.save()
    return rep


def no_has_reg(request):
    return render(request, 'qr_code/qr_code_no_has_reg.html')


def registrar_presenca(matricula):
    freq = get_freq()
    if freq.ativa is False:
        salvo = False
    else:
        reg = Registro()
        reg.status = True
        reg.frequencia = freq
        reg.aluno = freq.disciplina.matricula_disciplinar.get(id=matricula)
        reg.peso = freq.hora_fim.hour - freq.hora_inicio.hour + 1
        reg.save()
        salvo = True
    return salvo


def register_expired(request):
    return render(request, 'qr_code/qr_code_register_expired.html', {})


def register(request):
    mat = ''
    if request.method == "POST":
        mat = request.POST.get("id_matricula")
    matricula = MatriculaDisciplinar.objects.get(id=mat)
    if ip_repetido(request, matricula) is True or aluno_registered(matricula) is True:
        return redirect('ip_blocked')
    else:
        reg = registrar_presenca(mat)
        if reg is False:
            return redirect('register_expired')
    aluno = matricula.aluno
    response = render_to_response('qr_code/qr_code_registered.html', {'aluno': aluno})
    response.set_cookie('aluno', aluno)
    response.set_cookie('matricula', mat)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
        mat = request.COOKIES['matricula']
        matricula = MatriculaDisciplinar.objects.get(id=mat)
        if ip_repetido(request, matricula) is True or aluno_registered(matricula) is True:
            return redirect('ip_blocked')
        else:
            reg = registrar_presenca(mat)
            if reg is False:
                return redirect('register_expired')
    else:
        return redirect('get_alunos')
    return render(request, 'qr_code/qr_code_registered.html', {'aluno': aluno})
