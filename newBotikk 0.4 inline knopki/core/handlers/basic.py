from aiogram import Bot
from aiogram.types import Message

from core.keyboards.reply import main_button, sel_kurs
from core.keyboards.inline import sel_grup


async def get_start(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.first_name}!\nРад тебя видеть!",reply_markup=main_button)

async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет {message.from_user.first_name}!")


async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Этот бот предназначен для того, чтобы студентики узнавали расписание\nОзнакомься:\n1)Никто не должен знать о бойцовском клубе\n2)Носи всегда с собой нож")

async def select_kurs(message: Message, bot: Bot):
    await message.answer("Пожалуйста,выбери свой курс",reply_markup=sel_kurs)

async def first_kurs(message: Message, bot: Bot):
    await message.answer("Пожалуйста,выбери свою группу 1 курса",reply_markup=sel_grup)
# async def get_group(message: Message, bot: Bot):
#     await bot
#json_str = json.dumps(message.dict(),default=str)
#    print(json_str)