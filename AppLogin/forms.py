from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    

#class Formslogin(forms.Form):
 #   email=forms.EmailField()
 #   passw=forms.CharField(max_length=50)