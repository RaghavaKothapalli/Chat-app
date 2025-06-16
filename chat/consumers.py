import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from asgiref.sync import sync_to_async

# Track online users per room
online_users = {}  # room_name: set of usernames

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.username = self.scope["user"].username

        # Add user to online list
        if self.room_name not in online_users:
            online_users[self.room_name] = set()
        online_users[self.room_name].add(self.username)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send_online_users()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        if self.room_name in online_users and self.username in online_users[self.room_name]:
            online_users[self.room_name].remove(self.username)
            await self.send_online_users()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        user = await self.get_user(username)
        await self.save_message(user, message, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'username': event['username']
        }))

    async def send_online_users(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'online_users',
                'users': list(online_users.get(self.room_name, []))
            }
        )

    async def online_users(self, event):
        await self.send(text_data=json.dumps({
            'type': 'userlist',
            'users': event['users']
        }))

    @sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)

    @sync_to_async
    def save_message(self, user, content, room):
        return Message.objects.create(user=user, content=content, room=room)
