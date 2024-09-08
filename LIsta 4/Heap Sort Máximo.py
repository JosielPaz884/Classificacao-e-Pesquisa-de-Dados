def heapifyMax(arr, n, i):
    max = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        max = left
    if right < n and arr[max] < arr[right]:
        max = right
    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapifyMax(arr, n, max)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapifyMax(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyMax(arr, i, 0)
    return arr

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    heapSort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
