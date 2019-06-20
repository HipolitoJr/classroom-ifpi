from django.db import models

# Create your models here.


class Link(models.Model):
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/', null=True, blank=True,
                            height_field=264, width_field=264, max_length=200)

    def __str__(self):
        return self.url


class Aluno(models.Model):
    class Meta:
        db_table = 'Aluno'
    nome = models.CharField(max_length=100)
    qr_id = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
