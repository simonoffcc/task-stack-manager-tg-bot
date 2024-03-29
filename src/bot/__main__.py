import sys
import locale
import asyncio
import logging

from aiogram import Bot
from redis.asyncio.client import Redis

from src.bot.dispatcher import get_dispatcher, get_redis_storage
from src.bot.structures.data_structure import TransferData
from src.configuration import conf
from src.simple_db.models import async_main
from src.db.database import create_async_engine


async def start_bot():
    # await async_main()
    bot = Bot(token=conf.bot.token)
    storage = get_redis_storage(
        redis=Redis(
            db=conf.redis.db,
            host=conf.redis.host,
            password=conf.redis.passwd,
            username=conf.redis.username,
            port=conf.redis.port,
        )
    )
    dp = get_dispatcher(storage=storage)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        **TransferData(
            engine=create_async_engine(url=conf.db.build_connection_str()),
        ),
    )


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    logging.basicConfig(level=conf.logging_level, stream=sys.stdout)
    asyncio.run(start_bot())
