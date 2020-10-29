from django import forms
from django.contrib.auth.models import User
from .models import trade,tradereq,Report

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class tradeform(forms.ModelForm):
    class Meta:
        model=trade
        fields = "__all__"

class requestsellform(forms.ModelForm):
    class Meta:
        model=trade
        fields = "__all__"

class tradereqform(forms.ModelForm):
    class Meta():
        model=tradereq
        fields=('receiver','action','stock','numberofstocks','priceperstock')

class reportform(forms.ModelForm):
    class Meta():
        model=Report
        fields=('reporting',)
