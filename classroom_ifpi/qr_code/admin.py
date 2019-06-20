from django.contrib import admin

# Register your models here.

from qr_code.models import Aluno, Link

admin.site.register(Aluno)
admin.site.register(Link)
