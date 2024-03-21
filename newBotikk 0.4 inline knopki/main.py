import logging

from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
from core.handlers.basic import get_start, get_hello, get_help, select_kurs, first_kurs
from aiogram.filters import Command, CommandStart
from core.settings import settings
from aiogram import F
from core.utils.commands import set_commands

from core.handlers.callback import select_group_callback

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.callback_query.register(select_group_callback, F.data.startswith('first_'))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(select_kurs, F.text == 'Выбор курса')
    dp.message.register(first_kurs, F.text == '1 курс')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())