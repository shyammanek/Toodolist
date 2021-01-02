from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todo_app.models import todolist,Document
from django.forms import ModelForm
#shyammanek007
# shyam007
class todoform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['name','mobile','done']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
