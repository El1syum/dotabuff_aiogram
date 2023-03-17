import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.handlers.cancel import cancel_handler
from scripts.get_pickrate_and_winrate import get_pickrate_and_winrate


class WinrateForm(StatesGroup):
    hero_name = State()


async def get_hero_name(message: types.Message):
    logging.info(message)

    await WinrateForm.hero_name.set()

    await message.answer('Write down hero name')


async def pickrate_and_winrate(message: types.Message, state: FSMContext):
    try:

        hero_name = message.text

        result = get_pickrate_and_winrate(hero_name)

        await message.answer(result)
    finally:
        await state.finish()


def register_pickrate_and_winrate(dp: Dispatcher):
    dp.register_message_handler(get_hero_name, Text(equals='4'))
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(pickrate_and_winrate, state=WinrateForm.hero_name)
