from django.db import models

# Create your models here.
from comum.models import Turma, Professor, Horario


class DeclaracaoAusencia(models.Model):

    justificativa = models.CharField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE,
                                  related_name='declaracao_ausencia')
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE,
                              related_name='declaracao_ausencia')
    horario = models.ForeignKey(Horario, null=False, blank=False, on_delete=models.CASCADE,
                                related_name='declaracao_ausencia')
    data_falta = models.DateField()
    data_declaracao = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.professor.nome + " - " + str(self.data_falta)


class DeclaracaoInteresse(models.Model):
    interessado = models.ForeignKey(Professor,on_delete=models.CASCADE, related_name='interessado', default='')
    turma = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name='declaracao_interessse')
    data_declaracao = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.interessado.nome

class AusenciaInteresse(models.Model):
    ausencia = models.ForeignKey(DeclaracaoAusencia, null=False, blank=False, on_delete=models.CASCADE,
                                 related_name='ausencia_interesse')
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    status = models.BooleanField()
    interessado = models.ForeignKey(DeclaracaoInteresse,  null=False, blank=False, on_delete=models.CASCADE,
                                    related_name='ausencia_interesse')
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.ausencia.declarador.ministrante