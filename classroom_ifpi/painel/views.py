from django.shortcuts import render

# Create your views here.
from comum.models import Turma


def painel(request):
    return render(request, 'base.html')

def list_turmas(request):
    turmas = get_turmas(request)
    return render(request,
                  'turmas.html',
                  {'titulo': 'Suas Turmas',
                   'turmas': turmas})



def get_turmas(request):
    turmas = Turma.objects.filter(ministrante=request.user.professor)
    return turmas