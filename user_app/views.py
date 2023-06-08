from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, PasswordChangeForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_app:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user_app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_app:profile')
        else:
            return render(request, 'user_app/login.html', {'error_message': 'Invalid username or password.'})
    
    return render(request, 'user_app/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('user_app:login')

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_app:profile')
    else:
        form = UserUpdateForm(instance=user)
    
    return render(request, 'user_app/profile.html', {'form': form})

@login_required
def change_password(request):
    user = request.user

    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user_app:profile')
    else:
        form = PasswordChangeForm(user)
    
    return render(request, 'user_app/change_password.html', {'form': form})
