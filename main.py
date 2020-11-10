from get_info import get_html
from get_info import get_products
from get_info import get_text

if __name__ == '__main__':
    shoe = input('What shoe would you like to search: ')

    print(get_products(get_html(shoe)))