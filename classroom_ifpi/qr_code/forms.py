from django import forms

from comum.models import MatriculaDisciplinar


class MatriculaDisciplinarForm(forms.Form):
    class Meta:
        model = MatriculaDisciplinar
        fields = ('aluno',)