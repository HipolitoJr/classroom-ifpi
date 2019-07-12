from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class DeclaracaoAusenciaSerializer(serializers.ModelSerializer):
    #professor = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='matricula')
    #turma = serializers.SlugRelatedField(queryset=Turma.objects.all(), slug_field='especificacao_disciplina')
    #horario = serializers.SlugRelatedField(queryset=Horario.objects.all(), slug_field='hora_inicio')
    class Meta:
        model = DeclaracaoAusencia
        fields = ('justificativa','turma','horario','data_falta','data_declaracao')

class AusenciaInteresseSerializer(serializers.ModelSerializer):
	#interessado = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='matricula')
	class Meta:
		model = AusenciaInteresse
		fields = ('ausencia','hora_inicio','hora_fim','status','interessado')


class DeclaracaoInteresseSerializer(serializers.ModelSerializer):
    declarador = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='matricula')
    class Meta:
        model = DeclaracaoInteresse
        fields = ('declarador','data_declaracao')
