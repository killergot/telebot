from aiogram import Bot,Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from config import TOKEN_ADMIN

from handler import *
from wordly import *

storage = MemoryStorage()

bot = Bot(TOKEN_ADMIN,parse_mode='HTML')
dp = Dispatcher(storage=storage)

def on_startup(): #эта функция в начале всегда(почитать про аргумент _)
    print('Я был запущен!!!!!')

dp.message.register(cancel_command,Command(commands=['cancel']))
dp.message.register(start_command,Command(commands=['start']))
dp.message.register(help_command,Command(commands=['help']))
dp.message.register(links_command,Command(commands=['links']))
dp.message.register(get_photo_command,Command(commands=['photo']))
dp.message.register(location_command,Command(commands=['location']))
dp.message.register(weather_command,Command(commands=['weather']))
dp.message.register(give_command,Command(commands=['give']))
dp.message.register(ban_command,F.text.lower() == "бан")
dp.message.register(echo_weather,basicState.weather)
dp.message.register(game_command,Command(commands=['game']))
dp.message.register(menu_command,gameState.menu,F.text.startswith('Загадать'))
dp.message.register(game_choice,gameState.choice)
dp.message.register(game_confirm,gameState.confirm)
dp.message.register(broadcast_command,basicState.broadcast)
dp.message.register(check_word,gameState.menu,F.text=='Угадываем')
dp.message.register(start_game,gameState.inGame)

@dp.callback_query(gameState.inGame)
async def basic_callback(callback: types.CallbackQuery):
    await callback.answer(text='Это просто буква, не тыкай')
    

@dp.callback_query()
async def photo_callback(callback: types.CallbackQuery):
    global monke # это очень плохо!!!!
    if callback.data == 'like':
        await callback.answer(text='Супер')
    elif callback.data == 'dislike':
        await callback.answer(text='Не супер совсем нет')
    elif callback.data == 'Другое фото':
        monke=random.choice(list(filter(lambda x: x!=monke,monkes)))
        await callback.message.edit_media(types.InputMediaPhoto(media=monke,
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
    on_startup()
    dp.run_polling(bot)