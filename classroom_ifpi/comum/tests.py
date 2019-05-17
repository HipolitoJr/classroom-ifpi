from django.test import TestCase
from model_mommy import mommy
from comum.models import Curso


class TesteCurso(TestCase):

   def setUp(self):
       self.curso = mommy.make(Curso, descricao = 'CURSO DE TESTES EM PYTHON', tipo = 'TN')

   def teste_curso_creation(self):
       self.assertTrue(isinstance(self.curso, Curso))