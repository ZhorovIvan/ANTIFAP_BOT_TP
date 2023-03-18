from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit
from utils.get_joke_from_api import get_joke


@rate_limit(2, 'joke_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='^[Аа]некдот$')
async def command_joke(message: types.Message):
    joke_type = '11'
    joke = await get_joke(joke_type)
    await message.answer(joke)


@rate_limit(2, 'toast_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='^[Тт]ост$')
async def command_toast(message: types.Message):
    toast_type = '16'
    toast = await get_joke(toast_type)
    await message.answer(toast)


@rate_limit(2, 'quote_ch')
@dp.message_handler(chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='^[Цц]итата$')
async def command_quote(message: types.Message):
    quote_type = '15'
    quote = await get_joke(quote_type)
    await message.answer(quote)    