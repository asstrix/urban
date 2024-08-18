from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse


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
            print(username, pwd,rep_pwd, age)
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