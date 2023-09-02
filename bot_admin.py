from aiogram import Bot,Dispatcher, executor, types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from bot_keyboard import kb_main,ikb
from config import TOKEN_ADMIN,monkes,HELP_COMMAND
import random

monke = random.choice(monkes)

bot = Bot(TOKEN_ADMIN)
dp = Dispatcher(bot)

async def on_startup(_): #эта функция в начале всегда(почитать про аргумент _)
    print('Я был запущен!!!!!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                            text='Добро пожаловать в братство',
                            reply_markup=kb_main)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,text=HELP_COMMAND,parse_mode='HTML')
    except ZeroDivisionError:
        await bot.send_message(message.chat.id,text=HELP_COMMAND+'Начните диалог с нашим ботом!',parse_mode='HTML')
        await message.delete()

@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                            text='Пока ничего нет')

@dp.message_handler(commands=['photo'])
async def get_photo_command(message: types.Message):
    global monke #это очень плохо
    await message.answer('Как тебе?',
                         reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id = message.chat.id,
                        photo=monke,
                        caption='Вот обезьянка',
                        reply_markup=ikb)
    monke = random.choice(monkes)

@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    await bot.send_location(chat_id = message.chat.id,
                            latitude = random.random() * 90,
                            longitude = random.random() * 180)

@dp.message_handler(text='бан')
async def ban_command(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id,photo=('https://sun9-64.userapi.com/impg/mS4p5IfwlNxxWoDCBxv6q3KTIimd-JdpuMw_tw/VaeuwbuY0PM.jpg?size=828x590&quality=95&sign=ad0d39b3d50be3814b435f77518aef1d&type=album'))

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Нет такого варианта!!!')

@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    global monke # это очень плохо!!!!
    if callback.data == '❤️':
        await callback.answer(text='Супер')
    elif callback.data == '👎🏾':
        await callback.answer(text='Не супер совсем нет')
    elif callback.data == 'Другое фото':
        monke=random.choice(list(filter(lambda x: x!=monke,monkes)))
        await callback.message.edit_media(types.InputMedia(media=monke,
                                                           type='photo',
                                                           caption='Вот другая обезьянка'),
                                          reply_markup=ikb)
        await callback.answer()
    else :
        await callback.message.answer(text = 'Вы вернулись в главное меню',
                                      reply_markup=kb_main)
        await callback.message.delete()
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup, skip_updates=True)