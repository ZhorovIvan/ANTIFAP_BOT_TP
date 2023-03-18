async def on_sturtup(dp):

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils import send_message_to_fappers
    send_message_to_fappers


async def on_shutdown(dp):
    from utils.notify_admins import on_finish_notify
    await on_finish_notify(dp)


if __name__ == '__main__':

    from aiogram import executor
    from loader import dp
    
    executor.start_polling(dp, on_startup=on_sturtup)