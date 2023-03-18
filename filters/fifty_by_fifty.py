from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import random

class GiveAnswer(BoundFilter):
    async def check(self, message: types.Message):
        # Bot will answer in 50% cases
        return random.randint(0, 1) == 1