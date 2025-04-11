from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_names = ["live_data_live_data"]

        for room_name in self.room_names:
            await self.channel_layer.group_add(
                room_name,
                self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):
        for room_name in self.room_names:
            await self.channel_layer.group_discard(
                room_name,
                self.channel_name
            )

    async def send_live_data(self, event):
        message = event['message']
        await self.send_json({'message': message})
