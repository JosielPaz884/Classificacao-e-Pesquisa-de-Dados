def quickSort(data, begin, end):
    if begin < end:
        pivot = partition(data, begin, end)
        quickSort(data, begin, pivot-1)
        quickSort(data, pivot+1, end)

def partition(data, begin, end):
    pivot = data[end]
    i = begin - 1
    for j in range(begin, end):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[end] = data[end], data[i+1]
    return i + 1

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    quickSort(data,0,len(data)-1)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
