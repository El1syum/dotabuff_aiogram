import logging

from aiogram import types, Dispatcher


async def itembuild(message: types.Message):
    logging.info(message)
    await message.reply(message.text)


def register_itembuild(dp: Dispatcher):
    dp.register_message_handler(itembuild)
