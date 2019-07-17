from django.db import models

# Create your models here.

from comum.models import MatriculaDisciplinar
from frequencia.models import Frequencia


class IPAdress(models.Model):
    ip = models.GenericIPAddressField()
    frequencia = models.ForeignKey(Frequencia, related_name='ip_adress', on_delete=models.CASCADE)
    matricula_disciplinar = models.ForeignKey(MatriculaDisciplinar, related_name='iṕ_adress',
                                              on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
