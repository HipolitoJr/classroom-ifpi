from rest_framework import generics
from django_filters import rest_framework as filters
from horarios.models import DeclaracaoAusencia, AusenciaInteresse, DeclaracaoInteresse
from horarios.serializers import *
from django.contrib.auth.models import User

# Create your views here.

class DeclaracaoAusenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeclaracaoAusencia.objects.all()
    serializer_class = DeclaracaoAusenciaSerializer
    serializer_detail_class = DeclaracaoAusenciaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'declaracao_ausencia-detail'


class DeclaracaoAusenciaList(generics.ListCreateAPIView):
    #queryset = DeclaracaoAusencia.objects.all()
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is None:
            queryset = DeclaracaoAusencia.objects.all()
        else:
            pass
        return queryset
    serializer_class = DeclaracaoAusenciaSerializer
    name = 'declaracao_ausencia-list'


class AusenciaInteresseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AusenciaInteresse.objects.all()
    serializer_class = AusenciaInteresseSerializer
    serializer_detail_class = AusenciaInteresseSerializer
    name = 'ausencia_interesse-detail'


class AusenciaInteresseList(generics.ListCreateAPIView):
    queryset = AusenciaInteresse.objects.all()
    serializer_class = AusenciaInteresseSerializer
    name = 'ausencia_interesse-list'


class DeclaracaoInteresseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeclaracaoInteresse.objects.all()
    serializer_class = DeclaracaoInteresseSerializer
    serializer_detail_class = DeclaracaoInteresseSerializer
    name = 'declaracao_interesse-detail'


class DeclaracaoInteresseList(generics.ListCreateAPIView):
    queryset = DeclaracaoInteresse.objects.all()
    serializer_class = DeclaracaoInteresseSerializer
    name = 'declaracao_interesse-list'