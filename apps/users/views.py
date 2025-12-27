from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
# Create your views here.


def show_login_page(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def show_registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)


def show_profile_page(request):
    return render(request, 'users/profile.html')


def logout_user(request):
    logout(request)
    return redirect('home')