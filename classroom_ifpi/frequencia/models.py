from django.db import models

# Create your models here.
from comum.models import Turma, MatriculaDisciplinar
from horarios.models import Horario


class Frequencia(models.Model):

    data = models.DateField()
    disciplina = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='frequencia')
    horario = models.ForeignKey(Horario, null=False, blank=False, on_delete=models.CASCADE, related_name='frequencia')
    registros = models.ManyToManyField(MatriculaDisciplinar, through='Registro')


class Registro(models.Model):

    status = models.BooleanField()
    aluno = models.ForeignKey(MatriculaDisciplinar, null=False, blank=False, on_delete=models.CASCADE, related_name='registro')
    frequencia = models.ForeignKey(Frequencia, null=False, blank=False, on_delete=models.CASCADE, related_name='registro')
    peso = models.IntegerField()