from rest_framework import serializers
from .models import *


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('__all__')


class AusenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ausencia
        fields = ('__all__')
