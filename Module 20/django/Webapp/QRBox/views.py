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
        fields = ('email', 'password1', 'password2')

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
    context['form'] = form
    return render(request, 'register.html', context)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'QRBox: Login'
        return context


class QRCodeForm(forms.Form):
    data = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Enter text or URL...',
        'class': 'form-control'
    }))


def main_page(request):
    title = 'QRBox: Create QR Code for free'
    context = {
        'title': title,
    }
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            # Handle form's data here
            data = form.cleaned_data['data']
            context['data'] = data
    else:
        form = QRCodeForm()
    context['form'] = form
    return render(request, 'main.html', context)

