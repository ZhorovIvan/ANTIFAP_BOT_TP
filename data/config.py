import os 
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS_ID = str(os.getenv("ADMINS_ID")).split(',')
WEBHOOKURL = str(os.getenv("WEBHOOKURL"))
HOST = str(os.getenv("HOST"))
PORT = int(os.getenv("PORT"))
API_URL_JOKES = str(os.getenv("API_URL_JOKES"))
# mysql
DB_NAME = str(os.getenv("DB_NAME"))
USER_NAME = str(os.getenv("USER_NAME"))
PASSWORD_MYSQL = str(os.getenv("PASSWORD_MYSQL"))
HOST_MYSQL = str(os.getenv("HOST_MYSQL"))
PORT_MYSQL = int(os.getenv("PORT_MYSQL"))
