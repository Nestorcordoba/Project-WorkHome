from django import forms

class Login(forms.Form):
    useremail=forms.EmailField()
    password=forms.CharField(max_length=50)