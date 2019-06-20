from django.contrib import admin

# Register your models here.
from .models import Curso, Professor, Disciplina, Aluno, Turma, MatriculaDisciplinar, Horario


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    pass

@admin.register(MatriculaDisciplinar)
class MatriculaDisciplinarAdmin(admin.ModelAdmin):
    pass

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass
