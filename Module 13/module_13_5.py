from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token='')
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


def keyboard():
    kb = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Calculate'),
            KeyboardButton(text='Information'),
        ]
    ], resize_keyboard=True
    )
    return kb


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    user_name = message['from']['first_name']
    await message.answer(f"Hello {user_name}!", reply_markup=keyboard())


@dp.message_handler(text='Information')
async def info(message):
    await message.answer('I\'m the bot helping your health')


@dp.message_handler(text='Calculate')
async def set_age(message):
    await message.answer('Enter your age:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Enter your height:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=int(message.text))
    await message.answer('Enter your weight:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    await UserState.weight.set()
    data = await state.get_data()
    result = 10 * data['weight'] + 6.25 * data['height'] - 5 * data['age']
    await message.answer(result)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)