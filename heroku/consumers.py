from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
from channels.consumer import AsyncConsumer
class test(AsyncConsumer):
    async def websocket_connect(self, event):
        print("conented",event)
        await self.send({
            "type": "websocket.accept",
        })

        await self.send({
            "type": "websocket.send",
            "text": "Web soccet works"
        })
    async def websocket_disconnect(self, event):
        await self.send({
            'type':'websocket.accept',
            'text':"Halloo"
        })