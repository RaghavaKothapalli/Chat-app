from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def chat_room(request):
    messages = Message.objects.select_related('user').order_by('timestamp')
    return render(request, 'chat/room.html', {
        'username': request.user.username,
        'messages': messages
    })