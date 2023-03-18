from aiogram import Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from peewee_async import Manager
from peewee import Model


class DataBase(BaseMiddleware):

    def __init__(self, dt: Model, manager_peewee : Manager):
        super().__init__()
        self.dt = dt
        self.manager_peewee = manager_peewee


    async def on_pre_process_update(self, update: types.Update, data: dict):
        await self.manager_peewee.create(self.dt, chat_id=str(update.message["chat"]["id"]), data=str(update))