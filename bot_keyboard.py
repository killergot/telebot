from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb_main = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='/game'),
        KeyboardButton(text='/help'),
        KeyboardButton(text='/photo')],[KeyboardButton(text='/location'),
        KeyboardButton(text='/give'),
        KeyboardButton(text='/weather')]],
        resize_keyboard=True
)

kb_game_main_bun = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Угадываем'),
        KeyboardButton(text='Загадать Господину')],
        [KeyboardButton(text='/cancel')]],
        resize_keyboard=True
)

kb_game_main = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Угадываем'),
        KeyboardButton(text='Загадать Дусе')],
        [KeyboardButton(text='/cancel')]],
        resize_keyboard=True   
)

kb_game_confirm = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Все верно'),
        KeyboardButton(text='Поменяем')],
        [KeyboardButton(text='/cancel')]],
        resize_keyboard=True
)

ikb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='❤️',callback_data='like'),
        InlineKeyboardButton(text='👎🏾',callback_data='dislike')],
                     [InlineKeyboardButton(text='Другое фото',callback_data='Другое фото')],
                     [InlineKeyboardButton(text='Главное меню',callback_data='Главное меню')]])

def create_inline_kb(tempStr : str) -> InlineKeyboardMarkup:
    keyboard : list[list[InlineKeyboardButton]] = [[],[],[],[],[]]
    counter = 1
    for i in tempStr:
        keyboard[counter // 8].append(InlineKeyboardButton(text=i,callback_data=i))
        counter+=1

    return InlineKeyboardMarkup(inline_keyboard=keyboard)



# ikb = InlineKeyboardBuilder()
# ikb.add(InlineKeyboardButton(text='❤️',callback_data='like'),
#         InlineKeyboardButton(text='👎🏾',callback_data='dislike'))
# ikb.add(InlineKeyboardButton(text='Другое фото',callback_data='Другое фото'))
# ikb.add(InlineKeyboardButton(text='Главное меню',callback_data='Главное меню'))