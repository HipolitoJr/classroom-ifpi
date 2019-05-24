from django.db import models

# Create your models here.
from comum.models import Turma, Professor


class Horario(models.Model):

    DIA_SEMANA_CHOICES = (
        ('SEGUNDA', 'Segunda Feira'),
        ('TERCA', 'Terça Feira'),
        ('QUARTA', 'Quarta Feira'),
        ('QUINTA', 'Quinta Feira'),
        ('SEXTA', 'Sexta Feira'),
    )

    dia_semana = models.CharField(max_length=7, choices=DIA_SEMANA_CHOICES, null=False, blank=False )
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='horario')


class Ausencia(models.Model):

    justificativa = models.CharField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE, related_name='ausencia')
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='ausencia')
    horario = models.ForeignKey(Horario, null= False, blank=False, on_delete=models.CASCADE, related_name='ausencia')