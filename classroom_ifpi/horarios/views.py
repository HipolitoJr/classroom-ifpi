from rest_framework import generics
from horarios.models import Horario, Ausencia
from horarios.serializers import HorarioSerializer, AusenciaSerializer

# Create your views here.

class HorarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Horario.objects.all()
	serializer_class = HorarioSerializer
	name = 'horario-detail'


class HorarioList(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    serializer_detail_class = HorarioSerializer
    name = 'horario-list'


class AusenciaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ausencia.objects.all()
	serializer_class = AusenciaSerializer
	name = 'ausencia-detail'


class AusenciaList(generics.ListCreateAPIView):
    queryset = Ausencia.objects.all()
    serializer_class = AusenciaSerializer
    serializer_detail_class = AusenciaSerializer
    name = 'ausencia-list'