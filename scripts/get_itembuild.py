import logging

import requests
from bs4 import BeautifulSoup

from scripts.data import hero_url, headers


def get_itembuild(hero_name):
    item_build = ''
    url = hero_url(hero_name)

    r = requests.get(url=url, headers=headers)
    if r.status_code == 404:
        return 'Check out your hero name'

    soup = BeautifulSoup(r.text, 'lxml')
    try:
        items = soup.find('div', class_='top-right').find('div', class_='kv').find_all('div',
                                                                                       class_='match-item-with-time')
        for item in items:
            item_name = item.find('a').get('href').split('/')[-1]

            timing = item.find('div', class_='time')
            if timing:
                timing = timing.text
            else:
                timing = 'not given'

            item_build += f'{item_name}: {timing}\n'
        item_build = f'{hero_name.capitalize()}\n\n' + item_build

        return item_build

    except Exception as e:
        logging.error(f'GET_ITEMBUILD ERROR!\n{e}')
        return 'An error occurred. Try to use func again. If it doesn\'t work, contact the creator'


if __name__ == '__main__':
    print(get_itembuild('arc-warden'))
