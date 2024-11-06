from aiogram import Bot, Dispatcher, types

# Замените "YOUR_TOKEN_HERE" на токен вашего бота
API_TOKEN = '6668418273:AAEA2Lm_UGvKboGtoXoEqgOfC9v0LwRYbgQ'

# Создаем объект бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик для любых входящих текстовых сообщений
async def echo_message(message: types.Message):
    # Отправляем обратно текст, который получил бот
    await message.answer(message.text)
dp.message.register(echo_message)
# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
