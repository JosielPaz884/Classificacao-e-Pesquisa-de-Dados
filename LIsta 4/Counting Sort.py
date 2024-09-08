def countingSort(arr):
    maxValue = max(arr)
    count = [0] * (maxValue + 1)
    for number in arr:
        count[number] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    sortedArr = [0] * len(arr)
    for number in arr:
        sortedArr[count[number] - 1] = number
        count[number] -= 1
    return sortedArr  

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    data = countingSort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
