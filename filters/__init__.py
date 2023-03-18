from aiogram import Dispatcher

from .ignore_user import IsIgnore
from .fifty_by_fifty import GiveAnswer

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsIgnore, GiveAnswer)