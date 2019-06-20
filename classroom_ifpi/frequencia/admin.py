from django.contrib import admin

# Register your models here.
from frequencia.models import Frequencia, Registro

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    pass

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    pass
