from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/messages/<chat_id>/', consumers.ChatConsumer.as_asgi()),
]