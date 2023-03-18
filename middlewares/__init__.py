from aiogram import Dispatcher
from .antiflood import ThrottlingMiddleware
from .database import DataBase
from loader import test_table, pewee_manager


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(DataBase(test_table, pewee_manager))