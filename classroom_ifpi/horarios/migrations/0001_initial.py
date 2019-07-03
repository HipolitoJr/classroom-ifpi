# Generated by Django 2.2.2 on 2019-06-30 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeclaracaoInteresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_declaracao', models.DateField()),
                ('declarador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declaracao_interessse', to='comum.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='DeclaracaoAusencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificativa', models.CharField(max_length=255)),
                ('data_falta', models.DateField()),
                ('data_declaracao', models.DateField()),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declaracao_ausencia', to='comum.Horario')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declaracao_ausencia', to='comum.Professor')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declaracao_ausencia', to='comum.Turma')),
            ],
        ),
        migrations.CreateModel(
            name='AusenciaInteresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('status', models.BooleanField()),
                ('ausencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ausencia_interesse', to='horarios.DeclaracaoAusencia')),
                ('interessado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ausencia_interesse', to='horarios.DeclaracaoInteresse')),
            ],
        ),
    ]