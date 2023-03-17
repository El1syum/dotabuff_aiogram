import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.handlers.cancel import cancel_handler
from scripts.get_itembuild import get_itembuild


class ItembuildForm(StatesGroup):
    hero_name = State()


async def get_hero_name(message: types.Message):
    logging.info(message)

    await ItembuildForm.hero_name.set()

    await message.answer('Write down hero name')


async def itembuild(message: types.Message, state: FSMContext):
    try:
        hero_name = '-'.join(message.text.split()).lower()

        itembuild_result = get_itembuild(hero_name)

        await message.answer(itembuild_result)
    finally:
        await state.finish()


def register_itembuild(dp: Dispatcher):
    dp.register_message_handler(get_hero_name, Text(equals='2'))
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(itembuild, state=ItembuildForm.hero_name)
