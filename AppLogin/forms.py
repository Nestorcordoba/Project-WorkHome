from django import forms

class Formslogin(forms.Form):
    useremail=forms.EmailField()
    password=forms.CharField(max_length=50)