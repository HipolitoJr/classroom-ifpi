from django.db import models

# Create your models here.
from comum.models import Turma


class Horario(models.Model):

    DIA_SEMANA_CHOICES = (
        ('SEGUNDA', 'Segunda Feira'),
        ('TERCA', 'Terça Feira'),
        ('QUARTA', 'Quarta Feira'),
        ('QUINTA', 'Quinta Feira'),
        ('SEXTA', 'Sexta Feira'),
    )

    dia_semana = models.CharField(max_length=7, choices=DIA_SEMANA_CHOICES, null=False, blank=False )
    horario_inicio = models.TimeField()
    hora_fim = models.TimeField()
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='horario')
