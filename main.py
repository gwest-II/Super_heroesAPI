import requests

TOKEN = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]

def requests_all(url_all):
    response = (requests.get(url) for url in url_all)
    return response

def parser():
    super_heroes = []
    intelligence_hero = 0
    name = ''
    for item in requests_all(urls):
        specifications = item.json()
        for powerstats in specifications['results']:
            super_heroes.append({
                'name': powerstats['name'],
                'intelligence': powerstats['powerstats']['intelligence']
            })
    for powerstats_intelligence in super_heroes:
        if intelligence_hero < int(powerstats_intelligence['intelligence']):
            intelligence_hero = int(powerstats_intelligence['intelligence'])
            name = powerstats_intelligence['name']
    print(f'Самый умный супергерой {name} его интелект равен:{intelligence_hero}')


if __name__ == '__main__':
    parser()