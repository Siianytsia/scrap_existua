import requests
from bs4 import BeautifulSoup as BS
from random import randint
import csv
import time

domen = 'https://dok.ua'


def RandomUserAgent():
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/17.0.898.0 Safari/536.1.0',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/36.0.845.0 Safari/537.0.1',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_6 rv:5.0; AB) AppleWebKit/538.2.1 (KHTML, like Gecko) Version/7.1.10 Safari/538.2.1',
        'Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.0.1 (KHTML, like Gecko) Chrome/14.0.853.0 Safari/535.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/26.0.809.0 Safari/535.1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/34.0.855.0 Safari/532.0.2',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/26.0.850.0 Safari/531.1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/31.0.838.0 Safari/537.2.1',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/15.0.801.0 Safari/537.1.1',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.1; .NET CLR 3.1.38130.6)',
        'Opera/9.36 (Windows NT 6.0; U; LT Presto/2.9.185 Version/10.00)',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_5 rv:5.0; TR) AppleWebKit/536.2.0 (KHTML, like Gecko) Version/4.0.0 Safari/536.2.0']

    return user_agents[randint(0, len(user_agents) - 1)]


def GetProxy():
    proxies_list = [
        'http://29696:Pw4hVnq1@195.123.255.146:2831/',
        'http://29696:Pw4hVnq1@195.123.199.142:2831/',
        'http://29696:Pw4hVnq1@185.112.15.68:2831/',
        'http://29696:Pw4hVnq1@195.123.194.31:2831/',
        'http://29696:Pw4hVnq1@185.112.12.225:2831/',
    ]
    return proxies_list[randint(0, len(proxies_list) - 1)]


def GetCategoriesUrls():
    headers = {
        'Accept': '*/*',
        'User-Agent': RandomUserAgent()
    }

    subcategories_urls = []

    for i in range(1, 9):
        url = f'https://dok.ua/ua/rubrika/{i}'
        req = requests.get(url=url, headers=headers)
        print(req)
        soup = BS(req.text, 'lxml')
        name_category = soup.find('h1', {'class': 'main-title'}).find('strong').text.strip()
        a_tags_list = soup.find('div', {'class': 'rubric'}).find_all('a')
        urls = [('_'.join(name_category.split()), '_'.join(a.text.strip().split()), domen + a.get('href')) for a in a_tags_list if a.get('href')]
        for u in urls:
            subcategories_urls.append(u)

    with open('categories_urls.txt', 'w', encoding='utf-8') as file:
        for url in subcategories_urls:
            file.write(f'{url[0]} {url[1]} {url[2]}\n')


def main():
    GetCategoriesUrls()


if __name__ == '__main__':
    main()
