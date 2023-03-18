import logging
from aiogram import Dispatcher
from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(chat_id=admin, text='Бот запущен')
        except Exception as ex:
            logging.exception(ex)


async def on_finish_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(chat_id=admin, text='Бот остановлен')
        except Exception as ex:
            logging.exception(ex)
