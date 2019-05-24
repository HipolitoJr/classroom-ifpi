from rest_framework import serializers
from .models import *

class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = ('__all__')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('__all__')
