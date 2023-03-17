from scripts.get_hero_list import get_hero_list


def get_top_winrate():
    heroes_list = []

    heroes = get_hero_list()
    for hero in heroes:
        hero_name = '-'.join(hero.get('Name').split())
        hero_winrate = hero.get('Winrate')
        hero_stat = f'{hero_name}: {hero_winrate}'
        heroes_list.append(hero_stat)

    return ', '.join(heroes_list)


if __name__ == '__main__':
    get_top_winrate()
