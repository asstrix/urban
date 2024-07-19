from aiogram import Bot, Dispatcher
from aiogram.utils import executor

api = '7490221133:AAG4JGi-WGKsb_4x2wXjAjLRdz08OBltTMY'

bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def any_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)