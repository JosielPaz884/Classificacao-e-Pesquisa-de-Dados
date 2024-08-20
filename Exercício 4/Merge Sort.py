def merge(data, inicio, meio, fim):
    esquerda = data[inicio:meio + 1]
    direita = data[meio + 1:fim + 1]
    esquerda_index = 0
    direita_index = 0
    data_index = inicio
    while esquerda_index < len(esquerda) and direita_index < len(direita):
        if esquerda[esquerda_index] <= direita[direita_index]:
            data[data_index] = esquerda[esquerda_index]
            esquerda_index += 1
        else:
            data[data_index] = direita[direita_index]
            direita_index += 1
        data_index += 1
    while esquerda_index < len(esquerda):
        data[data_index] = esquerda[esquerda_index]
        esquerda_index += 1
        data_index += 1
    while direita_index < len(direita):
        data[data_index] = direita[direita_index]
        direita_index += 1
        data_index += 1

def mergeSort(data, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergeSort(data, inicio, meio)
        mergeSort(data, meio + 1, fim)
        merge(data, inicio, meio, fim)
    return data

def main():
    n = int(input("Digite a quantidade de elementos:"))
    data = []
    for i in range(n):
        x = int(input("Digite o elemento:"))
        data.append(x)
    
    print(f"Lista original:\n{data}")
    print(f"Lista ordenada:\n{mergeSort(data, 0, len(data) - 1)}")

if __name__== "__main__":
    main()
