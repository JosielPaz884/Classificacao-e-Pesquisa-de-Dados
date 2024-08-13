def selectionSort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i],data[min_idx] = data[min_idx],data[i]
    return data

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    selectionSort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
