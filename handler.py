from aiogram import types,Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps
from bot_keyboard import kb_main,ikb
from config import TOKEN_OWM,monkes,HELP_COMMAND
import random

monke : str = random.choice(monkes)

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM(TOKEN_OWM)
mgr = owm.weather_manager()

class basicState(StatesGroup):
    weather = State()
    broadcast = State()

async def start_command(message: types.Message,bot:Bot):
    await bot.send_message(chat_id=message.chat.id,
                            text='Добро пожаловать в братство',
                            reply_markup=kb_main)

async def help_command( message: types.Message,bot:Bot):
    try:
        await bot.send_message(message.from_user.id,text=HELP_COMMAND)
    except:
        await bot.send_message(message.chat.id,text=HELP_COMMAND+'Начните диалог с нашим ботом!')
        await message.delete()

async def links_command(message: types.Message,bot:Bot):
    await bot.send_message(chat_id=message.chat.id,
                            text='Пока ничего нет',
                            reply_markup=kb_main)

async def get_photo_command(message: types.Message,bot:Bot):
    global monke #это очень плохо
    await message.answer('Как тебе?',
                         reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id = message.chat.id,
                        photo=monke,
                        caption='Вот обезьянка',
                        reply_markup=ikb)
    monke = random.choice(monkes)

async def location_command(message: types.Message,bot:Bot):
    await bot.send_location(chat_id = message.chat.id,
                            latitude = random.random() * 90,
                            longitude = random.random() * 180,
                            reply_markup=kb_main)

async def weather_command(message: types.Message,bot:Bot,state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Введите название города:',
                           reply_markup=ReplyKeyboardRemove())
    await state.set_state(basicState.weather)
    

async def give_command(message: types.Message,bot:Bot,state: FSMContext):
    if message.from_user.id == 932481272:
        await bot.send_message(chat_id=message.chat.id,
                           text='Введите сообщение, которое хотите передать своему господину: ',
                           reply_markup=ReplyKeyboardRemove())
    else:
         await bot.send_message( chat_id=message.chat.id,
                           text='Введите сообщение, которое хотите передать своей булочке: ',
                           reply_markup=ReplyKeyboardRemove())
    await state.set_state(basicState.broadcast)
    
async def ban_command(message: types.Message,bot:Bot):
    await bot.send_photo(chat_id = message.chat.id,
                         photo=('https://sun9-64.userapi.com/impg/mS4p5IfwlNxxWoDCBxv6q3KTIimd-JdpuMw_tw/VaeuwbuY0PM.jpg?size=828x590&quality=95&sign=ad0d39b3d50be3814b435f77518aef1d&type=album'),
                         reply_markup=kb_main)

async def echo_weather(message: types.Message,bot:Bot, state: FSMContext):
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather 
        text:str=f"""Погода в городе {message.text}:
            Температура - {w.temperature('celsius')['temp']},
            Скорость ветра - {w.wind()['speed']}
            В городе сейчас {w.detailed_status}"""
    except:
        await bot.send_message(chat_id=message.chat.id,
                            text='Неверно введен город, попробуйте еще раз!')
    else:
        await bot.send_message(chat_id=message.chat.id,
                            text=text,
                            reply_markup=kb_main)
        await state.clear()

async def broadcast_command(message: types.Message,bot:Bot, state: FSMContext):
    if message.chat.id == 932481272:
        try:
            await message.send_copy(chat_id=588564125)
            await bot.send_message(chat_id=message.chat.id,
                                   text='Переданно успешно',
                                   reply_markup=kb_main)
            await state.clear()
        except:
            await bot.send_message(chat_id=message.chat.id,
                                   text='Произошла ошибка, поменяй что-то и пробуй еще раз')
    else:
        try:
            await message.send_copy(chat_id=932481272)
            await bot.send_message(chat_id=message.chat.id,
                                   text='Переданно успешно',
                                   reply_markup=kb_main)
            await state.clear()
        except:
            await bot.send_message(chat_id=message.chat.id,
                                   text='Произошла ошибка, поменяй что-то и пробуй еще раз')