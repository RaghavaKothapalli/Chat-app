from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def chat_room(request):
    room_name = request.GET.get('room', 'general')  # default: general
    messages = Message.objects.filter(room=room_name).order_by('timestamp')
    return render(request, 'chat/room.html', {
        'username': request.user.username,
        'messages': messages,
        'room_name': room_name,
    })