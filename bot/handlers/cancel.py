import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.buttons.common.menu import menu_buttons


async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('Cancelled.', reply_markup=menu_buttons())
