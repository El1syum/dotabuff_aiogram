import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.common.menu import menu_buttons


async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    if not state:
        await message.answer('Nothing to cancel')
        return

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('Cancelled.', reply_markup=menu_buttons())


async def empty_cancel(message: types.Message):
    await message.answer('Nothing to cancel')


def register_cancel(dp: Dispatcher):
    dp.register_message_handler(empty_cancel, commands=['cancel'])
    dp.register_message_handler(empty_cancel, Text(equals='cancel', ignore_case=True))
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')

