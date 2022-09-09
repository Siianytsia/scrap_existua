import requests
from bs4 import BeautifulSoup as BS
from random import randint
from datetime import datetime
import time
import csv
import asyncio
import aiohttp


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


headers = {
    'Accept': '*/*',
    'User-Agent': RandomUserAgent()
}

domen = 'https://exist.ua/'

def get_data():

    counter = 1
    ind = 0
    with open('subcategories_urls.txt', 'r', encoding='utf-8') as file:
        url = file.readlines()[ind]
        req = requests.get(url=url.strip(), headers=headers)
        src = req.text
        soup = BS(src, 'lxml')

        pages_amount = int(soup.find('a', {'aria-label': 'lastPage'}).text)

        with open(f'data\product_{counter}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            products_urls = []
            for i in range(1, pages_amount): #pages_amount
                req = requests.get(url=url.strip() + f'?page={i}', headers=headers)
                print(req)
                src = req.text
                soup = BS(src, 'lxml')

                urls_ = soup.find_all('a', {'aria-label': 'image'})
                urls = []
                for a in urls_:
                    u = domen + a.get('href')
                    urls.append(u)

                for u in urls:
                    products_urls.append(u)

            wrt = csv.writer(csvfile)
            wrt.writerow(
                (
                    'Артикул',
                    'Бренд',
                    'Название',
                    'Ссылка на фото'
                    # 'Название основные',
                    # 'Описание',
                    # 'Значение',
                    # 'Аналоги (артикул)',
                    # 'Аналоги (бренд)',
                    # 'Оригинальные номера',
                    # 'МАРКА',
                    # 'МОДЕЛЬ',
                    # 'ТИП МОДЕЛИ'
                )
            )

            for url in products_urls:
                req = requests.get(url=url.strip(), headers=headers)
                src = req.text
                soup = BS(src, 'lxml')

                vencode = soup.find('div', {'id': 'page-title'}).find('h1').text.split('\xa0')[0].split()[-1] if soup.find('div', {'id': 'page-title'}) is not None and soup.find('div', {'id': 'page-title'}).find('h1') is not None else ' '
                brand = soup.find('div', {'id': 'page-title'}).find_all('span')[0].find('strong').text if soup.find('div', {'id': 'page-title'}) is not None and soup.find('div', {'id': 'page-title'}).find_all('span')[0] is not None and soup.find('div', {'id': 'page-title'}).find_all('span')[0].find('strong') is not None else ' '
                name = soup.find('div', {'id': 'page-title'}).find('h1').text.split('\xa0')[0] if soup.find('div', {'id': 'page-title'}) is not None and soup.find('div', {'id': 'page-title'}).find('h1') is not None else ' '
                photo_link = soup.find('div', {'data-slide': 'true'}).find('img').get('src') if soup.find('div', {'data-slide': 'true'}) is not None and soup.find('div', {'data-slide': 'true'}).find('img') is not None else ' '

                wrt.writerow(
                    (
                        vencode,
                        brand,
                        name,
                        photo_link
                    )
                )

def main():
    start_time = datetime.now()
    get_data()
    print(datetime.now() - start_time)

if __name__ == '__main__':
    main()




