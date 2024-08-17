from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Login')
    password = forms.CharField(min_length=8, label='Password')
    repeat_password = forms.CharField(max_length=8, label='Repeat password')
    age = forms.CharField(max_length=3, label='Age')