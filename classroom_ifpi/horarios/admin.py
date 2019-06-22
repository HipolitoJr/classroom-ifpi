from django.contrib import admin

# Register your models here.
from horarios.models import DeclaracaoInteresse, DeclaracaoAusencia, AusenciaInteresse

@admin.register(DeclaracaoAusencia)
class DeclaracaoAusenciaAdmin(admin.ModelAdmin):
    pass

@admin.register(AusenciaInteresse)
class AusenciaInteresseAdmin(admin.ModelAdmin):
    pass

@admin.register(DeclaracaoInteresse)
class DeclaracaoInteresseAdmin(admin.ModelAdmin):
    pass