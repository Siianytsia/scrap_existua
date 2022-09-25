from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS
from random import randint
import time
import csv

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


def GetData():

    ind = 64    
    main_headers = {
        'Accept': '*/*',
        'User-Agent': RandomUserAgent()
    }

    main_proxy = {
        'http': GetProxy(),
        'https': GetProxy()
    }

    with open('categories_urls.txt', 'r', encoding='utf-8') as file:
        info = file.readlines()[ind].split()
        url = info[2]
        print(url)
        req = requests.get(url=url, headers=main_headers, proxies=main_proxy)
        soup = BS(req.text, 'lxml')

        pages_amount = int(soup.find('li', {'class': 'last'}).find('a').text)
        print(pages_amount)

        with open(f'data/{info[0]}/{info[1]}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            wrt = csv.writer(csvfile)
            wrt.writerow(
                (
                    'Артикул',
                    'Бренд',
                    'Название',
                    'Ссылка на фото',
                    'Характеристики',
                    'Аналоги',
                    'Марка',
                    'Модель'
                )
            )

            for i in range(1, pages_amount + 1):
                headers = {
                    'Accept': '*/*',
                    'User-Agent': RandomUserAgent()
                }

                proxies = {
                    'http': GetProxy(),
                    'https': GetProxy()
                }

                try:
                    pagination_url = url + f'?page={i}'
                    req = requests.get(url=pagination_url, headers=headers, proxies=proxies)
                    soup = BS(req.text, 'lxml')

                    products_urls = soup.find_all('a', {'class': 'product-card__layout-name'})
                    products_urls = [
                        (domen + a.get('href'), a.find('span', {'class': 'product-card__title'}).text.strip())
                        for a in products_urls if a.get('href')
                    ]
                    for item in products_urls:
                        u = item[0]

                        header = {
                            'Accept': '*/*',
                            'User-Agent': RandomUserAgent()
                        }

                        proxy = {
                            'http': GetProxy(),
                            'https': GetProxy()
                        }

                        req = requests.get(url=u, headers=header, proxies=proxy)
                        if str(req) == '<Response [404]>' or str(req) == '<Response [403]>':
                            print(req)
                            continue
                        if str(req) != '<Response [200]>':
                            print(req)
                            while str(req) != '<Response [200]>':
                                req = requests.get(url=u.strip(), headers=header, proxies=proxy)
                                time.sleep(0.3)
                            print(req)

                        soup = BS(req.text, 'lxml')

                        # Артикул
                        if soup.find('p', {'class': 'expert-numbers'}):
                            vencode = soup.find('p', {'class': 'expert-numbers'}).text.split()[-1]
                        elif soup.find_all('div', {'class': 'card-characts-list-item'}):
                            if len(soup.find_all('div', {'class': 'card-characts-list-item'})) >= 2:
                                if soup.find_all('div', {'class': 'card-characts-list-item'})[1].find('div', {
                                    'class': 'card-characts-list-item__text'}):
                                    vencode = soup.find_all('div', {'class': 'card-characts-list-item'})[1].find('div', {
                                        'class': 'card-characts-list-item__text'}).text.strip()
                        else:
                            vencode = ' '

                        # Бренд
                        brand = item[1]

                        # Название
                        if soup.find('div', {'class': 'card-title-box'}).find('h1').find('strong').text:
                            name = soup.find('div', {'class': 'card-title-box'}).find('h1').find('strong').text
                        else:
                            name = soup.find('div', {'class': 'card-title-box'}).find('h1').find('strong').find_all(
                                'span')
                            name = [t.text for t in name]
                            name = ' '.join(name)

                        # Ссылка на фото
                        photo_link = ' '
                        if soup.find('div', {'class': 'card-gallery-big'}) and soup.find('div', {
                            'class': 'card-gallery-big'}).find('img'):
                            photo_link = soup.find('div', {'class': 'card-gallery-big'}).find('img').get('content')

                        # Характеристики
                        characteristics_list = ' '
                        if soup.find('section', {'class': 'card-characts'}) and soup.find('section', {
                            'class': 'card-characts'}).find('div', {
                            'class': 'card-characts-list'}):
                            characteristics_list = soup.find('section', {'class': 'card-characts'}).find('div', {
                                'class': 'card-characts-list'}).find_all('div', {'class': 'card-characts-list-item'})
                            characteristics_list = [
                                f"Автозапчастини:{item.find('span', {'class': 'mistake-char-title'}).text.strip()}: {item.find('div', {'class': 'card-characts-list-item__text'}).text.strip()}|\n"
                                for item in characteristics_list
                            ]

                            characteristics_list = ''.join(characteristics_list)

                        # Аналоги
                        analogue_list = ' '
                        if soup.find('div', {'class': 'expert-analogs'}):
                            analogue_list = soup.find('div', {'class': 'expert-analogs'}).find('div', {
                                'class': 'catalog__product-list-row'}).find_all('div', {'class': 'product-card'})
                            analogue_list = [
                                f"{item.find('span', {'class': 'product-card__title'}).text.strip()} {item.find('span', {'class': 'product-card__serie'}).text.strip()[1:-1]}|\n"
                                for item in analogue_list
                            ]
                            analogue_list = ''.join(analogue_list)

                        # Марка
                        marks = ''
                        marks_table = []
                        if soup.find('div', {'class': 'expert-applicability-wrap'}):
                            marks_table = soup.find('div', {'class': 'expert-applicability-wrap'}).find_all('div', {
                                'class': 'expert-applicability'})
                            marks = [
                                f"{item.find('div', {'class': 'expert-applicability-title'}).get('id')}|\n"
                                for item in marks_table
                            ]
                            marks = ''.join(marks)

                        # модель
                        model = ''
                        if marks_table:
                            for mark in marks_table:
                                models_table = mark.find('table', {'class': 'expert-applicability-table'}).find_all(
                                    'tr', {'class': 'expert-applicability-table-tr_link'})
                                models_table = [
                                    f"{m.find('td', {'class': 'expert-applicability-table-model'}).find('span').text.strip()} {m.find('td', {'class': 'expert-applicability-table-body'}).text.strip()} {m.find('td', {'class': 'expert-applicability-table-release'}).text.strip()},\n"
                                    for m in models_table
                                ]
                                models_table = list(set(models_table))
                                for m in models_table:
                                    model += m
                                model = model[:-2] + '|\n'

                        wrt.writerow(
                            (
                                vencode,
                                brand,
                                name,
                                photo_link,
                                characteristics_list,
                                analogue_list,
                                marks,
                                model
                            )
                        )
                except requests.adapters.ConnectionError:
                    time.sleep(1)


def main():
    start_time = datetime.now()
    GetData()
    print(datetime.now() - start_time)


if __name__ == '__main__':
    main()