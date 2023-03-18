import aiohttp
import json
from data import config


async def get_joke(number: str):
    '''
    1 - Анекдот;
    2 - Рассказы;
    3 - Стишки;
    4 - Афоризмы;
    5 - Цитаты;
    6 - Тосты;
    8 - Статусы;
    11 - Анекдот (+18);
    12 - Рассказы (+18);
    13 - Стишки (+18);
    14 - Афоризмы (+18);
    15 - Цитаты (+18);
    16 - Тосты (+18);
    18 - Статусы (+18);
    '''
    url = config.API_URL_JOKES + number
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            json_obj = json.loads(html, strict=False)
            return json_obj["content"]

