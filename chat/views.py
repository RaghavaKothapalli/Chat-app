### chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login as auth_login
from .models import Message

# Homepage
def index(request):
    return render(request, 'chat/index.html')

# Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('/')

# Chat room
@login_required
def chat_room(request):
    room_name = request.GET.get('room', 'general')
    messages = Message.objects.filter(room=room_name).order_by('timestamp')
    return render(request, 'chat/room.html', {
        'username': request.user.username,
        'messages': messages,
        'room_name': room_name,
    })


### chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_room, name='chat'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]