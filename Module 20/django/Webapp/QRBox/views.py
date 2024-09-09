from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label=None)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def reg_page(request):
    title = 'QRBox: Register'
    context = {
        'title': title,
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'context': context})


class CustomLoginView(LoginView):
    template_name = 'login.html'


def main_page(request):
    title = 'QRBox'
    context = {
        'title': title,
    }
    return render(request, 'main.html', context)


def login_page(request):
    title = 'QRBox: Login'
    context = {
        'title': title,
    }
    return render(request, 'login.html', context)

