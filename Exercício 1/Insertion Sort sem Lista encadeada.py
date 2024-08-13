def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:  "))
    for i in range(n):
        element = int(input("Digite o elemento: "))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    insertionSort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
