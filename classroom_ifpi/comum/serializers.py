from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
        curso = serializers.SlugRelatedField(queryset=Curso.objects.all(), slug_field='disciplina')
        fields = ('matricula_curso','usuario','cpf','curso')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('matricula', 'usuario', 'cpf')

