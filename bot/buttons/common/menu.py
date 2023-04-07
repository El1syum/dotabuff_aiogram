from aiogram import types


def menu_buttons():
    kb = [
        [types.KeyboardButton(text='1'), types.KeyboardButton(text='2'),
         types.KeyboardButton(text='3'), types.KeyboardButton(text='4')],

        [types.KeyboardButton(text='Main menu')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder='Choose action')

    return keyboard
