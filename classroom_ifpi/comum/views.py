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

class DisciplinaView(viewsets.ModelViewSet):
	queryset = Disciplina.objects.all()
	serializer_class = DisciplinaSerializer
	serializer_detail_class = DisciplinaSerializer


class DisciplinaList(generics.ListCreateAPIView): 
	queryset = Disciplina.objects.all() 
	serializer_class = DisciplinaSerializer 
	name = 'disciplina-list'

class CursoView(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer
	serializer_detail_class = CursoSerializer


class CursoList(generics.ListCreateAPIView): 
	queryset = Curso.objects.all() 
	serializer_class = CursoSerializer 
	name = 'curso-list'


class TurmaView(viewsets.ModelViewSet):
	queryset = Turma.objects.all()
	serializer_class = TurmaSerializer
	serializer_detail_class = TurmaSerializer


class TurmaList(generics.ListCreateAPIView): 
	queryset = Turma.objects.all() 
	serializer_class = TurmaSerializer 
	name = 'turma-list'


class MatriculaDisciplinarView(viewsets.ModelViewSet):
	queryset = MatriculaDisciplinar.objects.all()
	serializer_class = MatriculaDisciplinarSerializer
	serializer_detail_class = MatriculaDisciplinarSerializer


class MatriculaDisciplinarList(generics.ListCreateAPIView): 
	queryset = MatriculaDisciplinar.objects.all() 
	serializer_class = MatriculaDisciplinarSerializer 
	name = 'matriculaDisciplinar-list'
