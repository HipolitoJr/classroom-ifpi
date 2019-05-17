from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from comum.models import Curso, Professor, Disciplina, Aluno, Turma, MatriculaDisciplinar
from django.utils.timezone import datetime


class TesteCurso(TestCase):

   def setUp(self):
       self.curso = mommy.make(Curso, descricao = 'CURSO DE TESTES EM PYTHON', tipo = 'TN')

   def teste_curso_creation(self):
       self.assertTrue(isinstance(self.curso, Curso))


class TesteUser(TestCase):

   def setUp(self):
       self.user = mommy.make(User, password = 'abcd1234', last_login = datetime.now(), is_superuser = False, username = 'teste', first_name = 'Teste' , last_name = 'User', email = 'teste@teste.com', is_staff = True, is_active = True, date_joined = datetime.now())

   def teste_user_creation(self):
       self.assertTrue(isinstance(self.user, User))



class TesteProfessor(TestCase):

   def setUp(self):
       self.user = mommy.make(User, password = 'abcd1234', last_login = datetime.now(), is_superuser = False, username = 'teste', first_name = 'Teste' , last_name = 'UserPROFESSOR', email = 'teste@teste.com', is_staff = True, is_active = True, date_joined = datetime.now())
       self.professor = mommy.make(Professor, usuario = self.user, matricula='TST2019', cpf = '123.456.789-09')

   def teste_professor_creation(self):
       self.assertTrue(isinstance(self.professor, Professor))

class TesteDisciplina(TestCase):

   def setUp(self):
       self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE')

   def teste_disciplina_creation(self):
       self.assertTrue(isinstance(self.disciplina, Disciplina))


class TesteAluno(TestCase):

   def setUp(self):
       self.user = mommy.make(User, password = 'abcd1234', last_login = datetime.now(), is_superuser = False, username = 'teste', first_name = 'Teste' , last_name = 'UserALUNO', email = 'teste@teste.com', is_staff = True, is_active = True, date_joined = datetime.now())
       self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON aluno', tipo='TN')
       self.aluno = mommy.make(Aluno, curso = self.curso, usuario = self.user, matriculaCurso='TSTA2019', cpf = '123.456.789-09')

   def teste_aluno_creation(self):
       self.assertTrue(isinstance(self.aluno, Aluno))


class TesteTurma(TestCase):

    def setUp(self):
        self.user = mommy.make(User, password='abcd1234', last_login=datetime.now(), is_superuser=False,
                               username='teste', first_name='Teste', last_name='UserMINISTRANTE', email='teste@teste.com',
                               is_staff=True, is_active=True, date_joined=datetime.now())
        self.professor = mommy.make(Professor, usuario=self.user, matricula='TST2019', cpf='123.456.789-09')
        self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE TURMA')
        self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON TURMA', tipo='TN')
        self.turma = mommy.make(Turma, cargaHoraria = 70, ministrante = self.professor, curso = self.curso, disciplina = self.disciplina)


class TesteMatriculaDisciplinar(TestCase):

    def setUp(self):
        self.user = mommy.make(User, password='abcd1234', last_login=datetime.now(), is_superuser=False,
                               username='teste', first_name='Teste', last_name='UserALUNO', email='teste@teste.com',
                               is_staff=True, is_active=True, date_joined=datetime.now())
        self.curso = mommy.make(Curso, descricao='CURSO DE TESTES EM PYTHON aluno', tipo='TN')
        self.aluno = mommy.make(Aluno, curso=self.curso, usuario=self.user, matriculaCurso='TSTA2019',
                                cpf='123.456.789-09')
        self.disciplina = mommy.make(Disciplina, descricao='DISCIPLINA TESTE')
        self.matriculaDisciplinar = mommy.make(MatriculaDisciplinar, aluno = self.aluno, disciplina = self.disciplina, situacao = 'C')