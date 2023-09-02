from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(KeyboardButton('/start'),
        KeyboardButton('/help'),
        KeyboardButton('/photo')).add(KeyboardButton('/location'),
        KeyboardButton('/give'),
        KeyboardButton('/links'))

ikb = InlineKeyboardMarkup()
ikb.add(InlineKeyboardButton(text='❤️',callback_data='❤️'),
        InlineKeyboardButton(text='👎🏾',callback_data='👎🏾'))
ikb.add(InlineKeyboardButton(text='Другое фото',callback_data='Другое фото'))
ikb.add(InlineKeyboardButton(text='Главное меню',callback_data='Главное меню'))
