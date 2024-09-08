def heapifyMin(arr, n, i):
    min = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] > arr[left]:
        min = left
    if right < n and arr[min] > arr[right]:
        min = right
    if min != i:
        arr[i], arr[min] = arr[min], arr[i]
        heapifyMin(arr, n, min)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapifyMin(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyMin(arr, i, 0)

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
