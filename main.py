from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='A KEY DO SEU BOT')
dp = Dispatcher(bot)

button1 = KeyboardButton(text="Random 1-10", callback_data="randomvalue_of10")
button2 = KeyboardButton(text="Random 1-100", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)


@dp.message_handler(commands='random')
async def aleatorio(message: types.message):
    await message.reply("Selecione um intervalo: ", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def bem_vindo(message: types.Message):
    await message.reply("Salve mano!! qm tá falando é o cauã na voz trazendo mais um Bot para vcs")


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def valor_aleatorio(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()


executor.start_polling(dp)

# @dp.message_handler(commands='info')
# async def info(message: types.message):
#     await message.reply('Fale alguma coisa sobre você', reply_markup=keyboard2)
#
#
# @dp.message_handler()
# async def resposta_teclado(message: types.message):
#     if message.text == 'salve!':
#         await message.answer('Salve man! Como vai pit?')
#     elif message.text == 'Github':
#         await message.answer('https://github.com/Cauanunes91')
#     else:
#         await message.answer(f'Your message is: {message.text} ')
