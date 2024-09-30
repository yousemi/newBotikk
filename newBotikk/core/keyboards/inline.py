from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
sel_grup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="18 группа",
            callback_data="first_18_группа"
        )

    ],
    [
        InlineKeyboardButton(
            text="ИС-1",
            callback_data="first_ИС-1_группа"
        )

    ],
[
        InlineKeyboardButton(
            text="ПК-1",
            callback_data="first_ПК-1_группа"
        )

    ]
])


sel_grup_2_kurs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="28 группа",
            callback_data="second_28_группа"
        )

    ],
    [
        InlineKeyboardButton(
            text="ИС-2",
            callback_data="second_ИС-2_группа"
        )

    ]
])



#[
#        InlineKeyboardButton(
#            text="",
#            url="https://патт.рф/"
#        )
#    ]
# sel_zayav = InlineKeyboardMarkup(inline_keyboard=[
#     [
#     InlineKeyboardButton(
#         text="Заявление причины отсутствия на парах",
#         callback_data="absence_from_class"
#     )
#     ],
#     [
#         InlineKeyboardButton(
#             text="В будущем можно добавить новые заявления",
#             callback_data="asas"
#         )
#     ]
# ])



sel_day = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Понедельник",
            callback_data="day_1"
        )

    ],
[
        InlineKeyboardButton(
            text="Вторник",
            callback_data="day_2"
        )

    ],
[
        InlineKeyboardButton(
            text="Среда",
            callback_data="day_3"
        )

    ],
[
        InlineKeyboardButton(
            text="Четверг",
            callback_data="day_4"
        )

    ],
[
        InlineKeyboardButton(
            text="Пятница",
            callback_data="day_5"
        )

    ],
[
        InlineKeyboardButton(
            text="Суббота",
            callback_data="day_6"
        )

    ],
])