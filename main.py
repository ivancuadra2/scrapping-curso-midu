
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

def main():
    # Example of a simple HTTP GET request
    response = requests.get(url)


    if response.status_code == 200:
        print('Success!')
        html = response.text
        sopa = BeautifulSoup(html, 'html.parser')
        # print(sopa.prettify())
        titulo = sopa.title.string
        padre = sopa.title.parent
        print('Title of the page:', titulo)
        print('Luke i am your father:', padre)
        # <span class="rc-prices-fullprice" data-autom="full-price">1.199,00 €</span> Este es el formato del precio
        # print(html)
        price_pattern = r'<span class="rc-prices-fullprice">(.*?) €</span>'
        prices = re.findall(price_pattern, html)
        if prices:
            print('Prices found:', len(prices))
            # for price in prices:
            #     print(price)
        else:
            print('No prices found.')
        # print(response.text)  Print the HTML content of the page
    else:
        print('Failed to retrieve data. Status code:', response.status_code)




if __name__ == "__main__":
    main()