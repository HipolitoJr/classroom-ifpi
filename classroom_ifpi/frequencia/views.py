from rest_framework import generics
from frequencia.models import Frequencia, Registro
from frequencia.serializers import FrequenciaSerializer, RegistroSerializer


# Create your views here.

class FrequenciaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Frequencia.objects.all()
	serializer_class = FrequenciaSerializer
	name = 'frequencia-detail'


class FrequenciaList(generics.ListCreateAPIView):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
    serializer_detail_class = FrequenciaSerializer
    name = 'frequencia-list'


class RegistroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer
	name = 'registro-detail'


class RegistroList(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    serializer_detail_class = RegistroSerializer
    name = 'registro-list'