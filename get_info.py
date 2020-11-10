from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_html(search):
    url = 'https://stockx.com/search/sneakers?s='
    url += '%20'.join(search.split())  # search url
    # print(url)

    options  = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = webdriver.Chrome(executable_path= r'C:\Users\Jacob\Documents\chromedriver_win32\chromedriver.exe',chrome_options=options)
    driver.get(url)
    #req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #page = urlopen(req).read()

    #return page.decode('utf-8')
    #return driver.page_source
    return driver.execute_script("return document.body.innerHTML")

def get_products(page):
    print(page)
    products = re.findall('<div>', page)
    return products

def get_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()