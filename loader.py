from aiogram import Bot, types, Dispatcher
from data import config
from utils.mysql.models import base_model
from utils.mysql import database
import peewee_async
from aiogram.contrib.fsm_storage.redis import RedisStorage2

#Mysql
db_mysql = database.mysql_db
test_table = base_model.TestDataModel
pewee_manager = peewee_async.Manager(db_mysql)
db_mysql.set_allow_sync(False)

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2(db=5)

dp = Dispatcher(bot, storage=storage)

# Mysql
# db = database.mysql_db
# t = base_model.BaseModel
# objects = peewee_async.Manager(db)
# db.set_allow_sync(False)