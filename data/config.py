import os 
from dotenv import load_dotenv
import ast

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS_ID = str(os.getenv("ADMINS_ID")).split(',')
CHAT_FAPPERS_ID = str(os.getenv("CHAT_FAPPERS_ID"))
TIME_FOR_LOG_NOTIFICATION = str(os.getenv("TIME_FOR_LOG_NOTIFICATION"))
USER_TIME_DATES = ast.literal_eval(os.environ["USER_TIME_DATES"])
USER_TIME_SMOKE = ast.literal_eval(os.environ["USER_TIME_SMOKE"])