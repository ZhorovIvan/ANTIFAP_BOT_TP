from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit


@rate_limit(2, '/help_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], text='/help')
async def help_channel(message: types.Message):
    await message.answer('анекдот - Пишет блять анекдот \n'
                         'тост - Пишет блять тост \n'
                         'цитата - Пишет цитата прости \n'
                         'Бот извинись - Пишет блять прости')