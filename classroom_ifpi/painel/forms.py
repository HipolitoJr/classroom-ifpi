from django import forms


class CadastrarProfessorForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.PasswordInput()
    confirma_password = forms.PasswordInput()
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    matricula = forms.CharField(required=True)


class CadastrarAlunoForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    matricula_curso = forms.CharField(required=True)
    curso = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)


class MatricularAlunoForm(forms.Form):

    aluno = forms.IntegerField(required=True)
    turma = forms.IntegerField(required=False)


class CadastrarTurmaForm(forms.Form):

    ministrante = forms.IntegerField(required=True)
    disciplina = forms.IntegerField(required=False)
    curso = forms.IntegerField(required=False)
    carga_horaria = forms.IntegerField(required=False)


class CadastrarCursoForm(forms.Form):

    descricao = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
