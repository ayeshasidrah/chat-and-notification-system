from django.urls import path, re_path
from .consumers import ChatConsumer, OnlineStatusConsumer, NotificationConsumer


websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    re_path(r"ws/online/", OnlineStatusConsumer.as_asgi()),
    re_path(r"ws/notify/", NotificationConsumer.as_asgi()),
]