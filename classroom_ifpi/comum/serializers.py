from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name')


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
        curso = serializers.SlugRelatedField(queryset=Curso.objects.all(), slug_field='disciplina')
        fields = ('matricula_curso','usuario','cpf','curso')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
        fields = ('matricula', 'cpf', 'usuario')


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        ministrantes = serializers.SlugRelatedField(queryset=Professor.objects.all(), many=True, slug_field='usuario.username')
        fields = ('descricao','ministrantes')


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        ministrante = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='usuario')
        disciplina = serializers.SlugRelatedField(queryset=Disciplina.objects.all(), slug_field='descricao')
        curso = serializers.SlugRelatedField(queryset=Curso.objects.all(), slug_field='disciplina')
        alunos = serializers.SlugRelatedField(queryset=MatriculaDisciplinar.objects.all(), slug_field='username')
        fields = ( 'especificacao_disciplina','carga_horaria','ministrante','disciplina', 'curso')


class MatriculaDisciplinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaDisciplinar
        aluno = serializers.SlugRelatedField(queryset=Aluno.objects.all(), slug_field='name')
        disciplina = serializers.SlugRelatedField(queryset=Disciplina.objects.all(), slug_field='descricao')
        fields = ('__all__')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('__all__')