from django.shortcuts import render
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'login.html'  # путь к вашему шаблону


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


def reg_page(request):
    title = 'QRBox: Register'
    context = {
        'title': title,
    }
    return render(request, 'register.html', context)

