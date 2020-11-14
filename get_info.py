from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_driver(user_driver):
    if user_driver != None:
        return user_driver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Jacob\Documents\chromedriver_win32\chromedriver.exe',
                              chrome_options=options)
    return driver


def get_html(search, user_driver=None):
    url = 'https://stockx.com/search/sneakers?s='
    url += '%20'.join(search.split())  # search url

    driver = get_driver(user_driver)
    driver.get(url)
    time.sleep(1)
    return driver.execute_script("return document.body.innerHTML")

def get_products(page):
    products = []
    soup = BeautifulSoup(page, 'html.parser')
    count = 0
    for i in soup.find_all("div", {"data-testid": "product-tile"}):
        if count == 5:
            break
        products.append(i.find('a').get('href'))
        count += 1
    return products

def get_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()

def get_product_page(suffix, user_driver=None):
    url = 'https://stockx.com' + suffix

    driver = get_driver(user_driver)

    driver.get(url)
    return driver.execute_script("return document.body.innerHTML")

def get_price(suffix, user_driver=None):
    url = 'https://stockx.com' + suffix

    driver = get_driver(user_driver)
    driver.get(url)
    prod_page = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(prod_page, 'html.parser')
    price = soup.find("div", {"class": "en-us stat-value stat-small"})
    return price.decode_contents()
