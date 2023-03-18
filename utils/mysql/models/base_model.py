from peewee import *
from utils.mysql.database import mysql_db
import peewee

class TestDataModel(peewee.Model):

    chat_id = peewee.CharField()
    data = peewee.TextField()

    class Meta:
        database = mysql_db