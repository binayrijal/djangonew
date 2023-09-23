from .models import User
from django import forms

from django.core import validators

class UserRegistration(forms.ModelForm):
    
    class Meta:
    
        model=User
        fields='__all__'
        widgets={
        'name': forms.TextInput( attrs= {'class':'form-control'}),
        'email': forms.TextInput(attrs= {'class':'form-control'}),
        'password': forms.PasswordInput(attrs= {'class':'form-control'}),
        
         }