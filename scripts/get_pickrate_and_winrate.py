import requests
from bs4 import BeautifulSoup

from scripts.data import hero_url, headers


def get_pickrate_and_winrate(hero_name):
    hero_info = [f'{hero_name.capitalize()}\n']
    hero = '-'.join(hero_name.split())

    url = hero_url(hero_name=hero)
    r = requests.get(url, headers=headers)
    if r.status_code == 404:
        return 'Check out hero name'

    soup = BeautifulSoup(r.text, 'lxml')
    container = soup.find('div', class_='col-8')
    lines_count = container.find_all('section')[0].find('article').find('table').find('tbody').find_all(
        'tr')
    for i in lines_count:
        td_list = i.find_all('td')
        hero_info.append(td_list[0].text)
        hero_info.append(f"Pickrate: {td_list[1].text}")
        hero_info.append(f"Winrate: {td_list[2].text}\n")
    popularity = 'Popularity: ', soup.find('div', class_='header-content-container').find('div',
                                                                                          class_='header-content-secondary').find(
        'dl').find('dd').text

    result = '\n'.join(hero_info) + '\n' + ''.join(popularity)

    return result


if __name__ == '__main__':
    print(get_pickrate_and_winrate('invoker'))
