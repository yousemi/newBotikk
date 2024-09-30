import sqlite3 as sq

db = sq.connect('C:/Users/YouSeMi/PycharmProjects/newBotikk/data.sqlite')

from aiogram import Bot, Dispatcher


async def change_group(id_bot, id_group):
    cur = db.cursor()
    cur.execute(f'UPDATE tg_id SET id_group_tg = {id_group} WHERE id = {id_bot}')
    db.commit()
    cur.close()

async def receiving_an_group_from_user(id_bot):
    cur = db.cursor()
    cur.execute(f'SELECT id_group_tg FROM tg_id WHERE id = {id_bot}')
    min_info = cur.fetchone()
    for info_of_group_user in min_info:
        return info_of_group_user

async def add_a_user_to_database(id_bot):
    cur = db.cursor()
    cur.execute(f'INSERT INTO tg_id (id, id_group_tg)VALUES ({id_bot}, 0) ON CONFLICT (id) DO NOTHING')
    db.commit()
    print('add user to db')


async def giving_an_raspis_to_user(day, id_group, bot: Bot, id_user):
    # Функция для отправки дня пользователю
    async def send_day_to_user(day):
        if day == '1':
            await bot.send_message(id_user, "Конечно, твое расписание на: Понедельник\n")
        elif day == '2':
            await bot.send_message(id_user, "Конечно, твое расписание на: Вторник\n")
        elif day == '3':
            await bot.send_message(id_user, "Конечно, твое расписание на: Среду\n")
        elif day == '4':
            await bot.send_message(id_user, "Конечно, твое расписание на: Четверг\n")
        elif day == '5':
            await bot.send_message(id_user, "Конечно, твое расписание на: Пятницу\n")
        elif day == '6':
            await bot.send_message(id_user, "Конечно, твое расписание на: Субботу\n")

    # Функция для получения расписания и отправки его пользователю
    async def send_raspis_with_day(day, id_group):
        cur = db.cursor()
        cur.execute(
            f'SELECT predmets.name, raspisanie.lessonsNamber, prepod.fio, raspisanie.cab '
            f'FROM raspisanie JOIN prepod ON raspisanie.id_prepod = prepod.id '
            f'JOIN predmets ON raspisanie.id_predmets = predmets.id '
            f'WHERE raspisanie.id_day = {day} AND raspisanie.id_grup = {id_group}')

        info = cur.fetchall()
        if info:
            await bot.send_message(id_user, "----------------------------------------------\nПара | Предмет | Преподаватель | Кабинет")
            for lesson in info:
                predmet = lesson[0]
                lesson_number = lesson[1]
                prepod = lesson[2]
                cab = lesson[3]
                # Форматируем и отправляем строку пользователю
                await bot.send_message(id_user, f"{lesson_number} | {predmet} | {prepod} | {cab}")
        else:
            await bot.send_message(id_user, "Нет расписания на выбранный день.")

    # Отправляем день и расписание пользователю
    await send_day_to_user(day)
    await send_raspis_with_day(day, id_group)