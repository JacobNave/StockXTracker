from urllib.request import urlopen
from urllib.request import Request
import re

def get_html(search):
    url = 'https://stockx.com/search/sneakers?s='
    url += '%20'.join(search.split())  # search url
    # print(url)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    return page.decode('utf-8')

def get_products(page):
    print(page)
    products = re.findall('<div>', page)
    return products

if __name__ == '__main__':
    shoe = input('What shoe would you like to search: ')


    print(get_products(get_html(shoe)))