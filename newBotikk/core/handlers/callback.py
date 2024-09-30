from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.types import FSInputFile
from core.middlewares.database import giving_an_raspis_to_user, receiving_an_group_from_user, change_group


async def select_group_callback(call: CallbackQuery, bot: Bot):
    kurs = call.data.split('_')[0]
    group = call.data.split('_')[1]
    id = call.from_user.id
    print(kurs, group)
    # обработчик расписания 1 курса:
    if kurs == 'first':
        # обработчик расписания 18 группы
        if group == '18':
            id_group = 3
            await call.message.answer(f'Твоя группа изменена на: {group}')
            await change_group(id, id_group)
        if group == 'ИС-1':
            id_group = 4
            await call.message.answer(f'Твоя группа изменена на: {group}')
            await change_group(id, id_group)
        if group == 'ПК-1':
            id_group = 5
            await call.message.answer(f'Твоя группа изменена на: {group}')
            await change_group(id, id_group)
    #2 kurs
    if kurs == 'second':
        if group == '28':
            id_group = 8
            await call.message.answer(f'Твоя группа изменена на: {group}')
            await change_group(id, id_group)
        if group == 'ИС-2':
            id_group = 9
            await call.message.answer(f'Твоя группа изменена на: {group}')
            await change_group(id, id_group)
        # обработчик другой группы




async def sel_zayav_callback(call: CallbackQuery, bot: Bot):
    reason = call.data.split('_')[0]
    photka = FSInputFile('C:/Users/YouSeMi/PycharmProjects/newBotikk/core/image/prich.jpg')
    if reason == 'absence':
        await call.message.answer('Пример заявления:')
        await call.message.answer_photo(photo=photka)
        await call.answer()



async def sel_day_callback(call: CallbackQuery, bot: Bot): #
    word_day = call.data.split('_')[0]
    day = call.data.split('_')[1]
    id_grup = await receiving_an_group_from_user(call.from_user.id)
    id_user = call.from_user.id
    await giving_an_raspis_to_user(day,id_grup,bot,id_user)
