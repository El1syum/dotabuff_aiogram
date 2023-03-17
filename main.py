import asyncio
import json
import logging
import os.path

from aiogram import Bot, Dispatcher, types

from bot.handlers.echo import register_echo
from bot.handlers.main_menu import register_main_menu
from bot.handlers.start import register_start
from bot.handlers.top_winrate import register_top_winrate

if not os.path.exists('logs/'):
    os.mkdir('logs')

logging.basicConfig(filename='logs/logs.log', level=logging.INFO, encoding='utf-8')

with open('config.json', 'r') as file:
    config = json.load(file)

TOKEN = config.get('TOKEN')

bot = Bot(token=TOKEN)


async def set_command(dp):
    bot_commands = [
        types.BotCommand(command="/start", description="Start polling"),
        types.BotCommand(command="/menu", description="Get menu"),
    ]
    await dp.bot.set_my_commands(bot_commands)


def register_all_handlers(dp):
    register_main_menu(dp)
    register_start(dp)
    register_top_winrate(dp)
    register_echo(dp)


async def main():
    dp = Dispatcher(bot=bot)
    register_all_handlers(dp)
    await set_command(dp)
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')