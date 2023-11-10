# meta developer: @random4ik_yt
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class irismoonbot(loader.Module):
    """Модуль для автоматического фарминга ic в боте @iris_moon_bot"""

    strings = {"name": "IrisFarmerbot"}

    def __init__(self):
        self.tasks = []

    async def work_run(self, client):
        while True:
            await client.send_message('@iris_moon_bot', "Работать")
            await asyncio.sleep(14401)

    @loader.unrestricted
    @loader.ratelimit
    async def irkafarmcmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Чел итак на полной катушке ._.")
        await message.edit("Окей летсгоу.")
        client = message.client
        self.tasks = [asyncio.create_task(self.work_run(client))]

    @loader.unrestricted
    @loader.ratelimit
    async def irkastopcmd(self, message):
        """Саня вырубай"""
        if not self.tasks:
            return await message.edit("Чел ты гений, или ты умеешь выключать то что уже выключено.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Наконецто.")