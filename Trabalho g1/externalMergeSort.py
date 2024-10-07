import re
import capturador

def merge_sort_external(prices, titles):
    if not prices:
        print("Não há preços para ordenar.")
        return

    prices = [float(re.search(r'\d+(,\d+)*', price).group().replace('.', '').replace(',', '.')) for price in prices]

    sorted_prices, sorted_titles = zip(*sorted(zip(prices, titles)))

    return sorted_prices, sorted_titles

def get_names(prices, titles):
    return titles

prices, titles = capturador.get_data('https://lista.mercadolivre.com.br/camiseta')

if prices is not None and titles is not None:
    sorted_prices, sorted_titles = merge_sort_external(prices, titles)

    if sorted_prices is not None and sorted_titles is not None:
        with open('precos_ordenados_com_nomes.txt', 'w') as f:
            for i, (price, title) in enumerate(zip(sorted_prices, sorted_titles)):
                f.write(f'Produto {i+1}: {title}, Preço: R${price:.2f}\n')
    else:
        print("Não há preços para ordenar.")
else:
    print("Erro ao obter dados.")