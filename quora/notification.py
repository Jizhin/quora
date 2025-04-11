from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
import asyncio

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Code to handle the WebSocket connection
        self.room_names = ["live_data_live_data"]

        # Join both room groups
        for room_name in self.room_names:
            await self.channel_layer.group_add(
                room_name ,
                self.channel_name
            )

        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_live_data(self, text_data):
        # Code to handle receiving WebSocket messages
        import time
        data = json.loads(text_data)
        if 'message' in data and data['message']:
            await self.send(text_data=json.dumps({
                'message': data.get('message')
            }))
