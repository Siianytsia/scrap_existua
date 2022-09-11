import requests
from bs4 import BeautifulSoup as BS
from random import randint
import time



def RandomUserAgent():
    user_agents = [ 'Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/17.0.898.0 Safari/536.1.0',
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

## получение html-кода главной страницы

# url = 'https://exist.ua/uk/avtozapchastyny/'
#
# req = requests.get(url=url, headers=headers)
# src = req.text
#
# with open('src.html', 'w', encoding='utf-8') as file:
#     file.write(src)

## получение файла с ссылками

# with open('src.html', 'r', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BS(src, 'lxml')
#
# categories = soup.find('div', class_='SparePartsstyle__SparePartsCatalogue-sc-13m5cdy-0').find_all('a')
#
# categories_urls = [domen + a.get('href') for a in categories][:-1]
#
# all_subcategories_urls = []
# for category_url in categories_urls:
#     req = requests.get(url=category_url, headers=headers)
#     src = req.text
#
#     soup = BS(src, 'lxml')
#
#     subcategories = soup.find_all('a', {'class': 'SparePartsItemstyle__SparePartsItemContainer-sc-4bv2fg-1'})
#
#     subcategories_urls = [domen + a.get('href') for a in subcategories]
#     print(subcategories_urls)
#
#     for url in subcategories_urls:
#         all_subcategories_urls.append(url)
#
#     time.sleep(1)
#
# all_subcategories_urls = list(set(all_subcategories_urls))
# print(len(all_subcategories_urls))
#
# with open('subcategories_urls.txt', 'w', encoding='utf-8') as file:
#     for url in all_subcategories_urls:
#         file.write(url + '\n')

# with open('subcategories_urls.txt', 'r', encoding='utf-8') as file:
#     counter = 1
#     for url in file.readlines()[:1]:
#         req = requests.get(url=url.strip(), headers=headers)
#         src = req.text
#         soup = BS(src, 'lxml')
#
#         pages_amount = int(soup.find('a', {'aria-label': 'lastPage'}).text)
#
#         with open(f'data\product_{counter}.txt', 'w', encoding='utf-8') as f:
#             products_urls = []
#             for i in range(1, pages_amount):
#                 req = requests.get(url=url.strip()+f'?page={i}', headers=headers)
#                 src = req.text
#                 soup = BS(src, 'lxml')
#
#                 urls_ = soup.find_all('a', {'aria-label': 'image'})
#                 urls = []
#                 for a in urls_:
#                     u = domen + a.get('href')
#                     urls.append(u)
#
#                 for u in urls:
#                     products_urls.append(u)
#
#             for line in products_urls:
#                 f.write(line+'\n')
#         counter += 1

with open('scraper2.py', 'r+', encoding='utf-8') as file:
    scr = file.readlines()
    with open('subcategories_urls.txt', 'r', encoding='utf-8') as urls_file:
        counter = 1
        for i in range(len(urls_file.readlines())):
            scr[36] = f'    counter = {counter}\n'
            scr[37] = f'    ind = {i}'
            with open(f'scripts/script_{counter}', 'w', encoding='utf-8') as script_file:
                for line in scr:
                    script_file.write(line)
            counter += 1

