from get_info import get_html
from get_info import get_products
from get_info import get_text
from get_info import get_product_page
from  get_info import get_price
from selenium import webdriver

if __name__ == '__main__':
    shoe = input('What shoe would you like to search: ')

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Jacob\Documents\chromedriver_win32\chromedriver.exe',
                              options=options)
    products = get_products(get_html(shoe, driver))
    for i in range(len(products)):
        print(str(i + 1) + ': ' + products[i])
    selection = int(input('\nChoose your best match: '))

    print(get_price(products[selection-1], driver))
