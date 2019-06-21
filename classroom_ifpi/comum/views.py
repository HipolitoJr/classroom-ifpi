from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, generics, authentication, permissions
from .serializers import *
from .models import *
from horarios import views as horario_views
from frequencia import views as frequencia_views


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'

	def get(self,request, *args, **kwargs):
		return Response({
			'usuarios': reverse(UserList.name,request=request),
			'professores': reverse(ProfessorList.name,request=request),
			'alunos': reverse(AlunoList.name,request=request),
			'disciplinas': reverse(DisciplinaList.name, request=request),
			'cursos': reverse(CursoList.name, request=request),
			'turmas': reverse(TurmaList.name, request=request),
			'matriculas': reverse(MatriculaDisciplinarList.name, request=request),
			'horarios': reverse(horario_views.HorarioList.name, request=request),
			'ausencias': reverse(horario_views.AusenciaList.name, request=request),
			'registros': reverse(frequencia_views.RegistroList.name, request=request),
			'frequencias': reverse(frequencia_views.FrequenciaList.name, request=request)
		})


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer
	serializer_detail_class = AlunoSerializer
	name = 'aluno-detail'


class AlunoList(generics.ListCreateAPIView): 
	queryset = Aluno.objects.all() 
	serializer_class = AlunoSerializer 
	name = 'aluno-list'


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializer
	serializer_detail_class = ProfessorSerializer
	name = 'professor-detail'


class ProfessorList(generics.ListCreateAPIView): 
	queryset = Professor.objects.all() 
	serializer_class = ProfessorSerializer 
	name = 'professor-list'


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Disciplina.objects.all()
	serializer_class = DisciplinaSerializer
	serializer_detail_class = DisciplinaSerializer
	name = 'disciplina-detail'


class DisciplinaList(generics.ListCreateAPIView): 
	queryset = Disciplina.objects.all() 
	serializer_class = DisciplinaSerializer 
	name = 'disciplina-list'


class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer
	serializer_detail_class = CursoSerializer
	name = 'curso-detail'


class CursoList(generics.ListCreateAPIView): 
	queryset = Curso.objects.all() 
	serializer_class = CursoSerializer 
	name = 'curso-list'


class TurmaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Turma.objects.all()
	serializer_class = TurmaSerializer
	serializer_detail_class = TurmaSerializer
	name = 'turma-detail'


class TurmaList(generics.ListCreateAPIView): 
	queryset = Turma.objects.all() 
	serializer_class = TurmaSerializer 
	name = 'turma-list'


class MatriculaDisciplinarDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MatriculaDisciplinar.objects.all()
	serializer_class = MatriculaDisciplinarSerializer
	serializer_detail_class = MatriculaDisciplinarSerializer
	name = 'matricula-disciplinar-detail'


class MatriculaDisciplinarList(generics.ListCreateAPIView): 
	queryset = MatriculaDisciplinar.objects.all() 
	serializer_class = MatriculaDisciplinarSerializer 
	name = 'matricula-disciplinar-list'
