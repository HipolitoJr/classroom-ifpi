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

    descricao = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=2, null=False, blank=False, choices=TIPO_CURSO_CHOICES, )

    def __str__(self):
        return self.descricao


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=15, null=False, blank=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
    cpf = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    descricao = models.CharField(max_length=100)
    ministrantes = models.ManyToManyField(Professor, through='Turma')

    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    nome = models.CharField(max_length=100, default='', null=True)
    matricula_curso = models.CharField(max_length=12, null=False, blank=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    cpf = models.CharField(max_length=14, null=False, blank=False)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    ministrante = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE, related_name='turma')
    especificacao_disciplina = models.CharField(max_length=100, null=False, blank=False)
    disciplina = models.ForeignKey(Disciplina, null=False, blank=False, on_delete=models.CASCADE, related_name='turma')
    carga_horaria = models.IntegerField()
    carga_horaria_ministrada = models.IntegerField(default=0)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, related_name='turma')
    alunos = models.ManyToManyField(Aluno, through='MatriculaDisciplinar')

    def __str__(self):
        return "%s - %s" % (self.especificacao_disciplina, self.curso.descricao)


class MatriculaDisciplinar(models.Model):
    SITUACAO_CHOICES = (
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
        ('C', 'Cursando'),
    )

    matricula = models.CharField(max_length=15, null=False, blank=False)
    aluno = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.CASCADE,
                              related_name='matricula_disciplinar')
    disciplina = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name='matricula_disciplinar')
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES, null=False, blank=False, default='C')

    def __str__(self):
        return self.aluno.nome+  " - " + self.disciplina.especificacao_disciplina


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

    def __str__(self):
        return self.dia_semana + " de " + str(self.hora_inicio)+' as '+str(self.hora_fim)
