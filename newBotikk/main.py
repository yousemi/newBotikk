
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import Command

from core.handlers.basic import get_start, get_hello, get_help, select_kurs, first_kurs, get_in_raspis, second_kurs
from core.handlers.callback import select_group_callback, sel_day_callback
from core.settings import settings
from core.utils.commands import set_commands



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
    dp.callback_query.register(select_group_callback, F.data.startswith('second_'))

    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_start, F.text == 'Вернуться в главное меню')

    dp.message.register(select_kurs, F.text == 'Выбор курса')
    dp.message.register(first_kurs, F.text == '1 курс')
    dp.message.register(second_kurs, F.text == '2 курс')


 #   dp.message.register(select_zayav, F.text == 'Заявления установленного образца')
 #   dp.callback_query.register(sel_zayav_callback, F.data.startswith('absence_'))

 #   dp.message.register(select_zayav, F.text == 'Режим работы и контактная информация административных отделений')

    dp.message.register(get_in_raspis, F.text == 'Узнать расписание')
    dp.callback_query.register(sel_day_callback, F.data.startswith('day_'))


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())