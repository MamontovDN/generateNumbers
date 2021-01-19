from django.urls import path

from number.consumers import NumConsumer

ws_urlpatterns = [
    path('ws/num/', NumConsumer.as_asgi())
]