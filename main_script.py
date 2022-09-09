import requests
from bs4 import BeautifulSoup as BS
from random import randint
import asyncio
import aiohttp

async def RandomUserAgent():
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