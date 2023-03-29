import asyncio
import aioschedule
from loader import bot
from data import config
import datetime

async def send_message():
    user_dates = config.USER_TIME_DATES
    private_date = config.USER_TIME_SMOKE
    text = '\n'.join([ get_text_message_for_fapper(user_name, user_dates[user_name]) for user_name in user_dates.keys() ])
    text += '\nНе хмурь бровей из-за ударов рока,\nУпавший духом, гибнет раньше срока.'
    days_without_smoke = (datetime.date.today() - datetime.date(year=int(private_date['Иван']["yyyy"]),month=int(private_date['Иван']["M"]),day=int(private_date['Иван']["dd"]))).days
    text += f'\n\nИван не курит кальян {days_without_smoke} дней.\nРви эту жизнь.'
    await bot.send_message(chat_id=config.CHAT_FAPPERS_ID, text=text)


def get_text_message_for_fapper(user_name, user_dates):
    days_without_fap = (datetime.date.today() - datetime.date(year=int(user_dates["yyyy"]),month=int(user_dates["M"]),day=int(user_dates["dd"]))).days
    return f"{user_name} не дрочил и не смотрел порно {days_without_fap} суток."


async def scheduler():
    aioschedule.every().day.at(config.TIME_FOR_LOG_NOTIFICATION).do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


asyncio.create_task(scheduler())
