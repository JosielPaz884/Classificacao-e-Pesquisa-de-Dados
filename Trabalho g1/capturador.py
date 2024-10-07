import requests
from bs4 import BeautifulSoup

def get_data(url):
    prices = []
    titles = []
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('div', class_='ui-search-result__content-wrapper')

        for product in products:
            price = product.find('div', class_='ui-search-price__second-line')
            title = product.find('a', class_='ui-search-link__title-card ui-search-link')
            if price and title:
                price = price.text.strip()
                title = title.text.strip()
                prices.append(price)
                titles.append(title)

        next_page = soup.find('a', class_='andes-pagination__button--next')
        if next_page:
            url = next_page.get('href')
        else:
            break

    with open('resultado.txt', 'w') as f:
        for i, (price, title) in enumerate(zip(prices, titles)):
            f.write(f'Título: {title}, Preço: {price}\n')

    return prices, titles