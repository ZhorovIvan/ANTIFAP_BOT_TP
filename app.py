async def on_sturtup(dp):
    from loader import bot, config
    await bot.set_webhook(config.WEBHOOKURL)

    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)


async def on_shutdown(dp):
    from utils.notify_admins import on_finish_notify
    await on_finish_notify(dp)

    from loader import bot, dp, db_mysql

    await db_mysql.close()
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram.utils.executor import start_webhook
    from aiogram import executor
    from handlers import dp
    from data import config
    
    start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_sturtup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=config.HOST,
        port=config.PORT,
    )
    # executor.start_polling(dp, on_startup=on_sturtup)