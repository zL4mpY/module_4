from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterForm

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    user_authenticated = request.user.is_authenticated
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('profile')
    return render(request, 'app_auth/login.html', {'error':'Пользователь не найден'})

def register_view(request):
    if request.method == "POST":
        regform = RegisterForm(request.POST)
        if regform.is_valid():
            user = regform.save()
            user.save()
            login(request, user)
            return redirect(reverse('profile'))
    else:
        regform = RegisterForm()
    context = {'form': regform}
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    return render(request, 'app_auth/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')