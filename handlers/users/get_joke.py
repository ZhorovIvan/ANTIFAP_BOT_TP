from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit
import random
from utils.get_joke_from_api import get_joke
from data import config


@rate_limit(5, 'joke_user')
@dp.message_handler(chat_type=[ChatType.PRIVATE], text='Бот напиши анекдот')
async def command_joke(message: types.Message):
    joke_type = '1' if random.randint(0, 1) == 1 else '11'
    joke = await get_joke(joke_type)
    await message.answer(joke)


@rate_limit(5, 'toast_user')
@dp.message_handler(chat_type=[ChatType.PRIVATE], text='Бот напиши тост')
async def command_toast(message: types.Message):
    toast_type = '6' if random.randint(0, 1) == 1 else '16'
    toast = await get_joke(toast_type)
    await message.answer(toast)


@rate_limit(5, 'nope_user')
@dp.message_handler(chat_type=[ChatType.PRIVATE],  regexp='[Нн]ет.*')
async def command_toast(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Пидора ответ')


@rate_limit(5, 'fatality_user')
@dp.message_handler(chat_type=[ChatType.PRIVATE], regexp='.*[шШ]люхи аргумент.*')
async def command_toast(message: types.Message):
    # Add filter on middleware
    if str(message["from"]["id"]) in config.ADMINS_ID:
        return
    await message.reply('Аргумент не нужен пидор обнаружен')