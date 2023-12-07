import json
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, UserModel, ChatNotification
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{str(self.room_name)}"
        # Join room group

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name)


        # Receive message from WebSocket
    async def receive(self, text_data=None,bytes_data = None):
        data = json.loads(text_data)
        message = data['message']
        self.user_id = self.scope['user'].id
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'user_id': self.user_id,
            }
        )

    def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        self.send(text_data=json.dumps({
            "message": message,
            "user_id": user_id,
        }))

    @database_sync_to_async
    def save_message(self, sender, receiver_username, message):
        receiver = User.objects.get(username=receiver_username)
        return Message.objects.create(sender=sender, receiver=receiver, content=message)


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        self.room_group_name = f'{my_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        count = data['count']
        print(count)
        await self.send(text_data=json.dumps({
            'count': count
        }))


class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'user'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        username = data['username']
        connection_type = data['type']
        print(connection_type)
        await self.change_online_status(username, connection_type)

    async def send_onlineStatus(self, event):
        data = json.loads(event.get('value'))
        username = data['username']
        online_status = data['status']
        await self.send(text_data=json.dumps({
            'username': username,
            'online_status': online_status
        }))

    async def disconnect(self, message):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def change_online_status(self, username, c_type):
        user = User.objects.get(username=username)
        userprofile = UserModel.objects.get(user=user)
        if c_type == 'open':
            userprofile.online_status = True
            userprofile.save()
        else:
            userprofile.online_status = False
            userprofile.save()