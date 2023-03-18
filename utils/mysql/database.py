from peewee import *
from data import config
import peewee_async

mysql_db = peewee_async.MySQLDatabase(config.DB_NAME, 
                        user=config.USER_NAME, 
                        password=config.PASSWORD_MYSQL,
                        host=config.HOST_MYSQL, 
                        port=config.PORT_MYSQL)
