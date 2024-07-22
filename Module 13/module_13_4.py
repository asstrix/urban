from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='')
dp = Dispatcher(bot,storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=int(message.text))
    await message.answer('Введите свой вес:')
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