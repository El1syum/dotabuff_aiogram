import logging

from aiogram import types, Dispatcher

from bot.buttons.common.menu import menu_buttons

menu_message = "Choose what do u want: \n\n" \
               "1. See who in the top by winrate now🔝\n" \
               "2. Get a itembuild of some hero👊\n" \
               "3. Look at the trends📈\n" \
               "4. Check a pickrate of some hero↗"


async def main_menu(message: types.Message):
    logging.info(message)
    await message.answer(menu_message, reply_markup=menu_buttons())


def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(main_menu, lambda message: message.text.lower() == 'main menu')
    dp.register_message_handler(main_menu, commands=['menu'])
