import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NumConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('gr_num', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('gr_num', self.channel_name)

    async def send_num(self, event):
        number = event['message']
        await self.send(number)


