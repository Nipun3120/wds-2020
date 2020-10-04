from django import forms
from django.contrib.auth.models import User
from .models import *

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class trade_form(forms.ModelForm):
    class Meta:
        model=trade
        fields = "__all__"
    
