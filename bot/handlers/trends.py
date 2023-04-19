import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.handlers.cancel import cancel_handler
from scripts.get_trends import get_trends


class TrendsForm(StatesGroup):
    count = State()


async def get_count(message: types.Message):
    logging.info(message)

    await TrendsForm.count.set()

    await message.answer('How many heroes do you want to see? (max: 15)')


async def trends(message: types.Message, state: FSMContext):
    count = message.text

    try:
        count = int(count)
    except ValueError:
        await message.answer('Count must be integer')
        return 0

    if count > 15:
        await message.answer('Count can\'t be more than 15')
        return 0

    trends_result = get_trends(count)

    await message.answer(trends_result)
    await state.finish()


def register_trends(dp: Dispatcher):
    dp.register_message_handler(get_count, Text(equals='3'))
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(trends, state=TrendsForm.count)
