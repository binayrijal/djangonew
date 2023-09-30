from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=50)
    
class Teacher(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=16)
    checkbox=models.BooleanField(default=False,null=False)