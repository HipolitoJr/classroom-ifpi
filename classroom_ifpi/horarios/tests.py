from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from comum.models import Disciplina, Professor, Curso, Turma
from django.utils.timezone import datetime

from horarios.models import Horario, Ausencia


class TesteHorario(TestCase):

    def setUp(self):
        self.user = mommy.make(User, password='abcd1234', last_login=datetime.now(), is_superuser=False,
                               username='teste', first_name='Teste', last_name='UserMINISTRANTE',
                               email='teste@teste.com',
                               is_staff=True, is_active=True, date_joined=datetime.now())
        self.professor = mommy.make(Professor, usuario=self.user, matricula='TST2019',
                                    cpf='123.456.789-09')
        self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE TURMA')
        self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON TURMA', tipo='TN')
        self.turma = mommy.make(Turma, especificacao_disciplina = 'Materia teste I',
                                carga_horaria=70, ministrante=self.professor, curso=self.curso,
                                disciplina=self.disciplina)

        self.horario = mommy.make(Horario, dia_semana='SEGUNDA', hora_inicio = datetime.now(), hora_fim = datetime.now(), turma = self.turma)

    def teste_horario_creation(self):
        self.assertTrue(isinstance(self.horario, Horario))


class TesteAusencia(TestCase):

    def setUp(self):
        self.user = mommy.make(User, password='abcd1234', last_login=datetime.now(), is_superuser=False,
                               username='teste', first_name='Teste', last_name='UserMINISTRANTE',
                               email='teste@teste.com',
                               is_staff=True, is_active=True, date_joined=datetime.now())
        self.professor = mommy.make(Professor, usuario=self.user, matricula='TST2019',
                                    cpf='123.456.789-09')
        self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE TURMA')
        self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON TURMA', tipo='TN')
        self.turma = mommy.make(Turma, especificacao_disciplina = 'Materia teste I',
                                carga_horaria=70, ministrante = self.professor, curso = self.curso,
                                disciplina = self.disciplina)

        self.horario = mommy.make(Horario, dia_semana='SEGUNDA', hora_inicio=datetime.now(), hora_fim=datetime.now(),
                                  turma=self.turma)

        self.ausencia = mommy.make(Ausencia, justificativa = 'justificativa teste', professor = self.professor, turma = self.turma, horario = self.horario)

    def teste_ausencia_creation(self):
        self.assertTrue(isinstance(self.ausencia , Ausencia))
