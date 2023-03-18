from aiogram import types
from loader import dp
from aiogram.types import ChatType
from utils.misc.throttling import rate_limit
from filters import IsIgnore, GiveAnswer


@rate_limit(20, 'nope_ch')
@dp.message_handler(GiveAnswer(), IsIgnore(),chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],  regexp='^[Нн]ет$')
async def command_toast(message: types.Message):
        await message.reply('Пидора ответ')  


@rate_limit(20, 'yaapkz_ch')
@dp.message_handler(GiveAnswer(), IsIgnore(), chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],  regexp='^[Дд]а$')
async def command_yaapkz(message: types.Message):
    await message.reply('Манда')


@rate_limit(20, 'fatality_ch')
@dp.message_handler(IsIgnore(), chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*[шШ]люхи аргумент.*')
async def command_toast(message: types.Message):
    await message.reply('Аргумент не нужен пидор обнаружен')
    # path for linux
    with open('/data/images/fatality.mp4', 'rb') as video:
        await message.answer_video(video)


@rate_limit(20, 'mom_ch')
@dp.message_handler(IsIgnore(), chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*([шШ]люха|[Пп]роститутка).*')
async def command_mom(message: types.Message):
    await message.reply('Шлюха твоя мамка' + message.from_user.full_name)


@rate_limit(20, 'big_mom_ch')
@dp.message_handler(IsIgnore(), chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL], regexp='.*([Жж]ирн(ая|ый|ое|ую)|[Тт]олст(ая|ый|ое|ую)).*')
async def command_big_mom(message: types.Message):
    await message.reply('Твоя мама такая толстая, что в ресторанах написано: \n'
                        '«Вместительность 300 человек, или твоя мама».')


@rate_limit(20, 'fuckbot_ch')
@dp.message_handler(IsIgnore(), chat_type=[ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL],  regexp='^([Пп]ошёл|[Ии]ди) ([Нн]ахуй|[Нн]ахер)$')
async def command_fuckbot(message: types.Message):
    await message.reply('Нахер твоя жопа хороша ' + message.from_user.full_name)