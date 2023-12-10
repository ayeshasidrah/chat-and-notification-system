from django.db import models
from django.db.models import (Model, TextField, DateTimeField, ForeignKey,
                              FileField, CASCADE, OneToOneField, SET_NULL, ManyToManyField
                              )

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model, decorators
from django.db import models
from accounts.models import User


# Create your models here.

class UserModel(Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(blank=True, null=True, max_length=225)
    online_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


class Message(Model):
    sender = ForeignKey(User, on_delete=CASCADE, related_name='sent_messages')
    mesage = models.TextField(null=True, blank=True)
    receiver = ForeignKey(User, on_delete=CASCADE, related_name='received_messages')
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mesage


class ChatNotification(models.Model):
    chat = ForeignKey(to=Message, on_delete=CASCADE)
    user = ForeignKey(to=User, on_delete=CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
