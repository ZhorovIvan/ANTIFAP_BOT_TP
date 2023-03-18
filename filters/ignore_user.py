from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from data import config

class IsIgnore(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id not in config.ADMINS_ID