from chat import consumers

from django.conf.urls import url

websocket_urlpatterns = [
    url('ws', consumers.ChatConsumer.as_asgi()),
]
