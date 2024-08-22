from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.
def main_page(request):
    title = 'Have a rest'
    header = 'Main Page'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, 'main.html', context)


def order_page(request):
    title = 'Orders: Have a rest'
    header = 'Orders'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, 'order.html', context)


def catalog_page(request):
    title = 'Catalog: Have a rest'
    header = 'Our games'
    games = Game.objects.all()
    context = {
        'title': title,
        'header': header,
        'games': games,
    }
    return render(request, 'catalog.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all().values_list('name', flat=True)
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            rep_pwd = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if pwd == rep_pwd and int(age) >= 18 and username not in users:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f"Hello, {username}!")
            elif username in users:
                info['error'] = 'User already exists'
            elif pwd != rep_pwd:
                info['error'] = 'Passwords do not match'
            elif int(age) < 18:
                info['error'] = 'You have to be older 18 years'
    else:
        form = UserRegister()
    context = {
        'info': info,
        'form': form,
    }
    return render(request, 'registration_page.html', context)