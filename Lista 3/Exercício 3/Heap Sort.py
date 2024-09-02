#Heapsort é um algoritmo de ordenação eficiente que utiliza um heap para ordenar uma lista de elementos.
def heapsort(data):
    buildHeap(data)
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, 0, i)

def buildHeap(data):
    for i in range(len(data) // 2 - 1, -1, -1):
        heapify(data, i, len(data))

def heapify(data, i, tamanho):
    maior = i
    esquerdo = 2 * i + 1
    direito = 2 * i + 2
    if esquerdo < tamanho and data[esquerdo] > data[maior]:
        maior = esquerdo
    if direito < tamanho and data[direito] > data[maior]:
        maior = direito
    if maior != i:
        data[i], data[maior] = data[maior], data[i]
        heapify(data, maior, tamanho)


def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    heapsort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
