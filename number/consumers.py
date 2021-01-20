import json

from channels.generic.websocket import AsyncWebsocketConsumer

from number.number_generator import MY_NUMBER


class NumConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('gr_num', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('gr_num', self.channel_name)

    async def receive(self, text_data=None):
        await self.send(str(MY_NUMBER[0]))

    async def send_num(self, event):
        number = event['message']
        await self.send(number)


