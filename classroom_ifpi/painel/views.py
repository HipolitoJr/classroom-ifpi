from django.shortcuts import render

# Create your views here.

def painel(request):
    return render(request, 'base.html')

def add_professor(request):
    return render(request, 'cadastro_professor.html')

def login(request):
    return render(request, 'login.html')