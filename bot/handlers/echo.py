import logging

from aiogram import types, Dispatcher


async def echo(message: types.Message):
    logging.info(message)
    await message.reply(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
