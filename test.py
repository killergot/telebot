# a = [1,2,3,4,5,6,7,8]
# b = list(filter(lambda x: x%2!=0,list(a)))
# print(b)
from aiogram import Dispatcher, executor,types,Bot
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import TOKEN_ADMIN,monkes
import random

bot = Bot(token=TOKEN_ADMIN)
dp = Dispatcher(bot=bot)

ikb=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❤️',callback_data='like'),
     InlineKeyboardButton(text='👎🏾',callback_data='dislike')],
    [InlineKeyboardButton(text='Закрыть все',callback_data='close')]
])

@dp.message_handler(commands=['start','help','give'])
async def get_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(monkes),
                         caption='Как тебе фото?',
                         reply_markup=ikb
                         )
    
@dp.callback_query_handler()
async def get_reaction(callback: types.CallbackQuery):
    if callback.data=='like':
        await callback.answer(text='Вам понравилось')
    elif callback.data=='dislike':
        await callback.answer(text='Вам не очень понравилось')
    else :
        await callback.message.edit_media(types.InputMedia(media=None,
                                                           type='photo',
                                                           caption='Вот другая обезьянка'),
                                          reply_markup=None)
        await callback.answer()
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)