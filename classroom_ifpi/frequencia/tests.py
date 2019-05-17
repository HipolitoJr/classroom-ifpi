from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from comum.models import Disciplina, Professor, Curso, Turma
from django.utils.timezone import datetime

from frequencia.models import Frequencia
from horarios.models import Horario


class TesteFrequencia(TestCase):

    def setUp(self):
        self.user = mommy.make(User, password='abcd1234', last_login=datetime.now(), is_superuser=False,
                               username='teste', first_name='Teste', last_name='UserMINISTRANTE',
                               email='teste@teste.com',
                               is_staff=True, is_active=True, date_joined=datetime.now())
        self.professor = mommy.make(Professor, usuario=self.user, matricula='TST2019', cpf='123.456.789-09')
        self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE TURMA')
        self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON TURMA', tipo='TN')
        self.turma = mommy.make(Turma, cargaHoraria=70, ministrante=self.professor, curso=self.curso,
                                disciplina=self.disciplina)

        self.horario = mommy.make(Horario, diaSemana='SEGUNDA', horaInicio=datetime.now(), dataFim=datetime.now(),
                                  turma=self.turma)
        self.frequencia = mommy.make(Frequencia, data = datetime.now(),disciplina = self.disciplina, horario = self.horario)