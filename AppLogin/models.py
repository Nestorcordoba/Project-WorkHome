from django.db import models

# Create your models here.

class Login(models.Model):
    useremail=models.EmailField()
    password=models.CharField(max_length=50)
