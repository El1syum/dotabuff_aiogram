import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from .data import WINRATE_URL


def get_hero_list():
    heroes_list = []
    url = WINRATE_URL

    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    heroes = soup.find('table', class_='sortable').find('tbody').find_all('tr')[:5]
    for hero in heroes:
        name = hero.find_all('td')[1].text
        winrate = hero.find_all('td')[2].text
        pickrate = hero.find_all('td')[3].text
        kda = hero.find_all('td')[4].text
        heroes_list += [
            {
                'Name': name,
                'Winrate': winrate,
                'Pickrate': pickrate,
                'KDA': kda
            }
        ]
    return heroes_list


if __name__ == '__main__':
    print(get_hero_list())
