from django.contrib import admin

# Register your models here.
from .models import Curso, Aluno


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Aluno)
class CursoAdmin(admin.ModelAdmin):
    pass