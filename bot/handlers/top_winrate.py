import logging

from aiogram import types, Dispatcher

from scripts.get_top_winrate import get_top_winrate


async def top_winrate(message: types.Message):
    logging.info(message)

    top_winrate_result = get_top_winrate()

    await message.answer(top_winrate_result)


def register_top_winrate(dp: Dispatcher):
    dp.register_message_handler(top_winrate, lambda message: message.text == '1')
