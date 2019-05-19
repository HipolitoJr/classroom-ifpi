from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *

class AlunoView(viewsets.ModelViewSet):
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer
	serializer_detail_class = AlunoSerializer


class AlunoList(generics.ListCreateAPIView): 
	queryset = Aluno.objects.all() 
	serializer_class = AlunoSerializer 
	name = 'aluno-list'

class ProfessorView(viewsets.ModelViewSet):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer
	serializer_detail_class = ProfessorSerializer


class ProfessorList(generics.ListCreateAPIView): 
	queryset = Professor.objects.all() 
	serializer_class = ProfessorSerializer 
	name = 'professor-list'
