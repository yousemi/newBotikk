from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery
from aiogram.types import  FSInputFile




async def select_group_callback(call: CallbackQuery, bot: Bot):
    kurs = call.data.split('_')[0]
    group = call.data.split('_')[1]
    textgruppa = call.data.split('_')[2]
    answer = f'Твоя {textgruppa} {group}'
    await call.message.answer(answer)
    await call.answer()

async def sel_zayav_callback(call: CallbackQuery, bot: Bot):
    reason = call.data.split('_')[0]
    photka = FSInputFile('C:/Users/Alexey/PycharmProjects/newBotikk/core/image/prich.jpg')
    if reason=='absence':
        await call.message.answer('Пример заявления:')
        await call.message.answer_photo(photo=photka)
        await call.answer()