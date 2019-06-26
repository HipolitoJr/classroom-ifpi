from rest_framework import serializers
from .models import *


class DeclaracaoAusenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclaracaoAusencia
        fields = ('__all__')

class AusenciaInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AusenciaInteresse
        fields = ('__all__')


class DeclaracaoInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclaracaoInteresse
        fields = ('__all__')
