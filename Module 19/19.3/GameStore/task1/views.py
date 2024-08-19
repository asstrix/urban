from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def main_page(request):
    title = 'F&F rent a car'
    header = 'Main Page'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, 'fourth_task/main.html', context)


def order_page(request):
    title = 'Orders: F&F rent a car'
    header = 'Orders'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, 'fourth_task/order.html', context)


def catalog_page(request):
    title = 'Catalog: F&F rent a car'
    header = 'Our cars'
    cars = ['Hyundai i30', 'Kia Stonic', 'Ford Focus', 'Skoda Scala', 'Ford Focus C-Max']
    context = {
        'title': title,
        'header': header,
        'cars': cars,
    }
    return render(request, 'fourth_task/catalog.html', context)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            rep_pwd = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if pwd == rep_pwd and int(age) >= 18 and username not in users:
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
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        rep_pwd = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if pwd == rep_pwd and int(age) >= 18 and username not in users:
            return HttpResponse(f"Hello, {username}!")
        elif username in users:
            info['error'] = 'User already exists'
        elif pwd != rep_pwd:
            info['error'] = 'Passwords do not match'
        elif int(age) < 18:
            info['error'] = 'You have to be older than 18 years'

    return render(request, 'fifth_task/registration_page.html', {'info': info})