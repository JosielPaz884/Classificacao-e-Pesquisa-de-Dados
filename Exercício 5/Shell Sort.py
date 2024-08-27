def shellSort(list):
    nCount=len(list)//2
    while nCount>0:
        for startIndex in range(nCount):
            jumpInsertionSort(list,startIndex,nCount)
        print(f"Incremento de tamanho:{nCount}\nLista é: {list}")
        nCount=nCount//2
    return list

def jumpInsertionSort(list,start,jump):
    for i in range(start+jump,len(list),jump):
        key=list[i]
        j=i
        while j>=jump and list[j-jump]>key:
            list[j]=list[j-jump]
            j-=jump
        list[j]=key
    return list

def main():
    data = []
    n = int(input("Digite a quantidade de elementos:"))
    for i in range(n):
        element = int(input("Digite o elemento:"))
        data.append(element)

    print("-----------------")
    print("Lista Original:", data)
    shellSort(data)
    print("-----------------")
    print("Lista Ordenada:", data)

if __name__ == "__main__":
    main()
