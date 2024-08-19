def bubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j]>data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
            
def main():
    data= []
    n= int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        x = int(input("Digite o elemento:"))
        data.append(x)
    
    print(f"Lista original:\n{data}")
    print(f"Lista ordenada:\n{bubbleSort(data)}")

if __name__== "__main__":
    main()
