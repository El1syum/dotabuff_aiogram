from fake_useragent import UserAgent

WINRATE_URL = 'https://ru.dotabuff.com/heroes/winning'
TRENDS_URL = 'https://www.dotabuff.com/heroes/trends'

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}


def hero_url(hero_name):
    return f'https://ru.dotabuff.com/heroes/{hero_name}'


if __name__ == '__main__':
    ...
