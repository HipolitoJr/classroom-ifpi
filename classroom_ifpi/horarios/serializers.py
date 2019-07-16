from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class DeclaracaoAusenciaSerializer(serializers.HyperlinkedModelSerializer):
    professor = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='nome')
    turma = serializers.SlugRelatedField(queryset=Turma.objects.all(), slug_field='especificacao_disciplina')
    #horario = serializers.SlugRelatedField(queryset=Horario.objects.all(), slug_field='hora_inicio')
    class Meta:
        model = DeclaracaoAusencia
        fields = ('url', 'id','justificativa','professor','turma','horario','data_falta')

class AusenciaInteresseSerializer(serializers.HyperlinkedModelSerializer):
	#interessado = serializers.SlugRelatedField(queryset=DeclaracaoInteresse.objects.all(), slug_field='interessado')
	class Meta:
		model = AusenciaInteresse
		fields = ('url', 'id','ausencia','hora_inicio','hora_fim','status','interessado')


class DeclaracaoInteresseSerializer(serializers.HyperlinkedModelSerializer):
    turma = serializers.SlugRelatedField(queryset=Turma.objects.all(), slug_field='especificacao_disciplina')
    class Meta:
        model = DeclaracaoInteresse
        fields = ('url', 'id','interessado','turma')
