from .models import User
from django import forms

from django.core import validators

class UserRegistration(forms.ModelForm):
    class meta:
        model=User
        fields='__all__'