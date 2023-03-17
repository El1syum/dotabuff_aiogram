import logging

from aiogram import types, Dispatcher

from bot.buttons.common.menu import menu_buttons

start_text = "Hello friend! I am simple, not official dotabuff bot. \n" \
             "With me you can get some info from Dotabuff.com! \n" \
             "Choose what do you want: \n\n" \
             "1. See who in the top by winrate now🔝\n" \
             "2. Get a itembuild of some hero👊\n" \
             "3. Look at the trends📈\n" \
             "4. Check a pickrate of some hero↗"


async def start(message: types.Message):
    logging.info(message)
    await message.answer(start_text, reply_markup=menu_buttons())


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
