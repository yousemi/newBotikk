from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Выбор курса'
        ),
        KeyboardButton(
            text='Узнать расписание'
        )
    ],
    [
        KeyboardButton(
            text='Режим работы и контактная информация административных отделений'
        ),
        KeyboardButton(
            text='Заявления установленного образца'
        )
    ],
    ])


sel_kurs = ReplyKeyboardMarkup(keyboard=[
    [
    KeyboardButton(
        text='1 курс',
    ),
    KeyboardButton(
        text='2 курс'
    )
    ],
    [
    KeyboardButton(
        text='3 курс'
    ),
    KeyboardButton(
        text='4 курс'
    )],
    [
    KeyboardButton(
        text='Вернуться в главное меню'
    )]
], one_time_keyboard=True)

