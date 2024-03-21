from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
sel_grup = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(
        text="14 группа",
        callback_data="first_14_группа"
    )
    ],
    [
        InlineKeyboardButton(
            text="16 группа",
            callback_data="first_16_группа"
        )
    ],
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




#[
#        InlineKeyboardButton(
#            text="Rot ebal lox ahah",
#            url="https://патт.рф/"
#        )
#    ]