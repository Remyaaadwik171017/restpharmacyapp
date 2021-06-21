from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    options=(("completed","completed"),
             ("notcompleted","notcompleted"))
    status=forms.ChoiceField(choices=options)
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control p-2"}),
            'last_name': forms.TextInput(attrs={"class": "form-control p-2"}),
            'email': forms.EmailInput(attrs={"class": "form-control p-2"}),
            'username': forms.TextInput(attrs={"class": "form-control p-2"}),
            'password1':forms.TextInput(attrs={"class":"form-control p-2"}),
            'password2':forms.TextInput(attrs={"class":"form-control p-2"})
        }
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

