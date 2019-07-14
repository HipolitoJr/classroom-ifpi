from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id','username','password','first_name', 'last_name')


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    curso = serializers.SlugRelatedField(queryset=Curso.objects.all(), slug_field='descricao')
    class Meta:
        model = Aluno
        fields = ('url','id','matricula_curso','usuario','cpf','curso')


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    class Meta:
        model = Professor
        usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
        fields = ('url','id','matricula', 'cpf', 'usuario')


class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        ministrantes = serializers.SlugRelatedField(queryset=Professor.objects.all(), many=True, slug_field='usuario.username')
        fields = ('url','id','descricao','ministrantes')


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    ministrante = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='nome')
    disciplina = serializers.SlugRelatedField(queryset=Disciplina.objects.all(), slug_field='descricao')
    curso = serializers.SlugRelatedField(queryset=Curso.objects.all(), slug_field='descricao')
    alunos = AlunoSerializer(many=True, read_only=True)
    class Meta:
        model = Turma
        fields = ('url','id','especificacao_disciplina','carga_horaria',
            'ministrante','disciplina', 'curso', 'alunos')


class MatriculaDisciplinarSerializer(serializers.HyperlinkedModelSerializer):
    aluno = serializers.SlugRelatedField(queryset=Aluno.objects.all(), slug_field='nome')
    disciplina = serializers.SlugRelatedField(queryset=Turma.objects.all(), slug_field='especificacao_disciplina')
    class Meta:
        model = MatriculaDisciplinar
        fields = ('url','id','aluno', 'disciplina')


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('url','id','descricao', 'tipo')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    turma = serializers.SlugRelatedField(queryset=Turma.objects.all(),slug_field='especificacao_disciplina')
    class Meta:
        model = Horario
        fields = ('url','id','dia_semana', 'hora_inicio','hora_fim', 'turma')