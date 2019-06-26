# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from comum.models import Aluno

def home(request):
    link = "http://192.168.43.174:8000/qr/registered"
    return render(request, 'qr_code/qr_code.html', {'link': link})


def register(request):
    aluno = ''
    alunos = Aluno.objects.all()
    response = render_to_response('qr_code/qr_code_register.html', {'alunos': alunos})
    response.set_cookie('aluno', aluno)
    return response


def registered(request):
    if 'aluno' in request.COOKIES:
        aluno = request.COOKIES['aluno']
    else:
        return redirect('register')
    return render(request, 'qr_code/qr_code_registered.html', {})
