from django.db import models

# Create your models here.
class User(models.Model):
    name=models.TextField(max_length=100)
    email=models.EmailField(max_length=30)
    password=models.TextField(max_length=50)
