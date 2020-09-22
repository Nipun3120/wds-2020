from django import forms

class RegisterForm(forms.Form):
    teamname = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    email = forms.EmailField(label='E-mail', required=True, max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)