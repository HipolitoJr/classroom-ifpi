from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Curso(models.Model):

  TIPO_CURSO_CHOICES = (
     ('TN', 'Técnico'),
     ('TG', 'Tecnologia'),
     ('BA', 'Bacharel'),
     ('LI', 'Licenciatura'),
     ('ME', 'Mestrado'),
  )

  descricao = models.CharField(max_length=100,  null=False, blank=False)
  tipo = models.CharField(max_length=2, null=False, blank=False, choices=TIPO_CURSO_CHOICES,)

  def __str__(self):
     return self.descricao



class Professor(models.Model):

  matricula = models.CharField(max_length=15, null=False, blank=False)
  usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
  cpf = models.CharField(max_length=14, null=False, blank=False)

  def __str__(self):
      return self.usuario.first_name + self.usuario.last_name


class Disciplina(models.Model):

  descricao = models.CharField(max_length=100)
  ministrantes = models.ManyToManyField(Professor, through='Turma')

  def __str__(self):
     return self.descricao


class Aluno(models.Model):

  matricula_curso = models.CharField(max_length=12, null=False, blank=False)
  usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
  cpf = models.CharField(max_length=14, null=False, blank=False)
  curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name= 'aluno')

  def __str__(self):
      return self.usuario.first_name + self.usuario.last_name

class Turma(models.Model):
  ministrante = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE, related_name= 'turma')
  especificacao_disciplina = models.CharField(max_length=100, null=False, blank=False)
  disciplina = models.ForeignKey(Disciplina, null=False, blank=False, on_delete=models.CASCADE, related_name= 'turma')
  carga_horaria = models.IntegerField()
  curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name='turma')
  alunos = models.ManyToManyField(Aluno, through='MatriculaDisciplinar')

  def __str__(self):
     return self.especificacao_disciplina


class MatriculaDisciplinar(models.Model):

  SITUACAO_CHOICES = (
      ('A', 'Aprovado'),
      ('R', 'Reprovado'),
      ('C', 'Cursando'),
  )

  matricula = models.CharField(max_length=15, null=False, blank=False)
  aluno = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.CASCADE, related_name='matricula_disciplinar')
  disciplina = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE, related_name='matricula_disciplinar')
  situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES, null=False, blank=False , default='C')