import logging

from aiogram import types, Dispatcher

from scripts.get_hero_list import get_hero_list


async def top_winrate(message: types.Message):
    logging.info(message)
    heroes_list = []

    heroes = get_hero_list()
    for hero in heroes:
        hero_name = '-'.join(hero.get('Name').split())
        hero_winrate = hero.get('Winrate')
        hero_stat = f'{hero_name}: {hero_winrate}'
        heroes_list.append(hero_stat)

    await message.answer(', '.join(heroes_list))


def register_top_winrate(dp: Dispatcher):
    dp.register_message_handler(top_winrate, lambda message: message.text == '1')
