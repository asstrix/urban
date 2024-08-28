from django.shortcuts import render


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

