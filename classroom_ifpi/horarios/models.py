from django.db import models

# Create your models here.
from classroom_ifpi.comum.models import Turma


class Horario(models.Model):

    DIA_SEMANA_CHOICES = (
        ('SEGUNDA', 'Segunda Feira'),
        ('TERCA', 'Terça Feira'),
        ('QUARTA', 'Quarta Feira'),
        ('QUINTA', 'Quinta Feira'),
        ('SEXTA', 'Sexta Feira'),
    )

    diaSemana = models.CharField(max_length=7, choices=DIA_SEMANA_CHOICES, null=False, blank=False )
    horarioInicio = models.TimeField()
    horaFim = models.TimeField()
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='horario')
