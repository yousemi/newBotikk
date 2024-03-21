from aiogram import Bot
from aiogram.types import CallbackQuery
async def select_group_callback(call: CallbackQuery, bot: Bot):
    kurs = call.data.split('_')[0]
    group = call.data.split('_')[1]
    textgruppa = call.data.split('_')[2]
    answer = f'Твоя {textgruppa} {group}'
    await call.message.answer(answer)
    await call.answer()