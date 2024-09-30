from aiogram import Bot
from aiogram.types import Message
from conda.core.link import messages

from core.keyboards.reply import main_button, sel_kurs
from core.keyboards.inline import sel_grup, sel_day, sel_grup_2_kurs
from core.middlewares.database import add_a_user_to_database, receiving_an_group_from_user
async def get_start(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.first_name}!\nРад тебя видеть!",reply_markup=main_button)
    await add_a_user_to_database(message.from_user.id)

async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет {message.from_user.first_name}!")


async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"---------------------------------------\nИнформация:\n\tДанный бот создан для того, чтобы представлять расписание студентам,а также информацию об изменениию. \n(Подсказка, если вы увидите , что номер пары совпадает, то у вас скорее всего будет пара в том или ином кабиенте)\n------------------------------\nКраткое сведение об техникуме:\n\tГБПОУ РО 'ПАТТ' Профессиональное образование это основная ступенька для дальнейшего карьерного роста. Наш техникум - это квалифицированные педагоги, современные профессиональные стандарты и материальная база, востребованные на рынке труда профессии и специальности, социальные партнеры и многое другое. В 2016 году наш Техникум прошёл процедуру общественной аккредитации образовательных программ")

async def select_kurs(message: Message, bot: Bot):
    await message.answer("Пожалуйста,выбери свой курс",reply_markup=sel_kurs, one_time_keyboard=True)

async def first_kurs(message: Message, bot: Bot):
    await message.answer("Пожалуйста,выбери свою группу 1 курса",reply_markup=sel_grup)

async def second_kurs(message: Message, bot: Bot):
    await message.answer("Пожалуйста,выбери свою группу 2 курса",reply_markup=sel_grup_2_kurs)

#async def select_zayav(message: Message, bot: Bot):
#    await message.answer("Выбери то заявление, которое вам нужно",reply_markup=sel_zayav)

async def text_for_jops_tech(message: Message, bot: Bot):
    await message.answer("Режим работы всего техникума с 8 до 20:00.")


async def get_in_raspis(message: Message, bot: Bot):
    id_user = await receiving_an_group_from_user(message.from_user.id)
    if id_user == 0:
        await message.answer("Прошу прощения. Сначала выберите группу.")
    elif id_user > 0:
        await message.answer("Конечно, на какой день тебя интересует расписание?", reply_markup=sel_day)




# async def get_group(message: Message, bot: Bot):
#     await bot
#json_str = json.dumps(message.dict(),default=str)
#    print(json_str)