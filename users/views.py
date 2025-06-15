from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import os
print("TEMPLATE DIRS = ", os.listdir("users/templates/users"))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'User created successfully!')
        return redirect('login')
    return render(request, 'users/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat')  # we’ll create this page later
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
