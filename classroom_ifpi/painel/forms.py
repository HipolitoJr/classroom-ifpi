from django import forms


class CadastrarProfessorForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.PasswordInput()
    confirma_password = forms.PasswordInput()
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    matricula = forms.CharField(required=True)