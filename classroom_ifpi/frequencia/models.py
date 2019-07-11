from django.db import models

# Create your models here.
from comum.models import Turma, MatriculaDisciplinar


class Frequencia(models.Model):

    data = models.DateField()
    disciplina = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='frequencia')
    # horario = models.ForeignKey(Horario, null=False, blank=False, on_delete=models.CASCADE, related_name='frequencia')
    registros = models.ManyToManyField(MatriculaDisciplinar, through='Registro')
    ativa = models.BooleanField(default=True)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return self.disciplina.especificacao_disciplina + " " + str(self.data) + " - " + str(self.hora_inicio)


class Registro(models.Model):

    status = models.BooleanField()
    aluno = models.ForeignKey(MatriculaDisciplinar, null=False, blank=False, on_delete=models.CASCADE, related_name='registro')
    frequencia = models.ForeignKey(Frequencia, null=False, blank=False, on_delete=models.CASCADE, related_name='registro')
    peso = models.IntegerField()

    def __str__(self):
        return str(self.aluno) + " - " + str(self.frequencia.data)