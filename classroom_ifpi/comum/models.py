from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Curso(models.Model):

   descricao = models.CharField(max_length=100,  null=False, blank=False)
   tipo = models.CharField(max_length=100)


class Professor(models.Model):

   matricula = models.CharField(max_length=15, null=False, blank=False)
   usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
   cpf = models.CharField(max_length=14, null=False, blank=False)


class Disciplina(models.Model):

   descricao = models.CharField(max_length=100)


class Aluno(models.Model):

   matriculaCurso = models.CharField(max_length=12, null=False, blank=False)
   usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
   cpf = models.CharField(max_length=14, null=False, blank=False)
   curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name= 'aluno')


class Turma(models.Model):
   ministrante = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE, related_name= 'turma')
   disciplina = models.ForeignKey(Disciplina, null=False, blank=False, on_delete=models.CASCADE, related_name= 'turma')
   cargaHoraria = models.IntegerField()
   curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name='turma')


class MatriculaDisciplinar(models.Model):

   SITUACAO_CHOICES = (
       ('A', 'Aprovado'),
       ('R', 'Reprovado'),
       ('C', 'Cursando'),
   )

   aluno = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.CASCADE, related_name='matriculaDisciplinar')
   disciplina = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='matriculaDisciplinar')
   situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES, null=False, blank=False , default='C')

