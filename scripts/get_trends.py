import requests
from bs4 import BeautifulSoup

from scripts.data import TRENDS_URL, headers


def get_trends(count):
    try:
        count = int(count)
    except TypeError:
        return 'Count must be integer'

    if count > 15:
        return 'Count can\'t be more than 15'

    message = ''

    r = requests.get(url=TRENDS_URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    cards = soup.find('table', class_='sortable').find('tbody').find_all('tr')[:count]
    for card in cards:
        hero_name = str(card.find('td', class_='cell-centered').get('data-value'))
        previous_percentage = round(float(card.find_all('td')[1].get('data-value')), 2)
        current_percentage = round(float(card.find_all('td')[2].get('data-value')), 2)
        change = round(current_percentage - previous_percentage, 2)
        message += f'Hero name: {hero_name}\nPrevious percentage: {previous_percentage}\nCurrent percentage: {current_percentage}\nChange: {change}\n\n'

    return message


if __name__ == '__main__':
    print(get_trends(15))
