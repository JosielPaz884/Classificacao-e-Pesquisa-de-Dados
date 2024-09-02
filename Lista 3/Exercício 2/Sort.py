import random
import time
import matplotlib as plt

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2

def gList(tipo, tamanho):
    if tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho - 1, -1, -1))
    elif tipo == 'repetida':
        return [random.randint(0, tamanho // 2) for _ in range(tamanho)]
    elif tipo == 'aleatoria':
        return [random.randint(0, tamanho) for _ in range(tamanho)]


def testAlgorit(tipo, tamanho):
    lista = gList(tipo, tamanho)
    algoritmos = {
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Shell Sort': shell_sort
    }
    resultados = {}
    for nome, algoritmo in algoritmos.items():
        inicio = time.time()
        algoritmo(lista.copy())
        fim = time.time()
        resultados[nome] = fim - inicio
    return resultados

tipos = ['ordenada', 'inversa', 'repetida', 'aleatoria']
tamanhos = [100, 500, 1000, 5000]
resultados = {}
for tipo in tipos:
    resultados[tipo] = {}
    for tamanho in tamanhos:
        resultados[tipo][tamanho] = testAlgorit(tipo, tamanho)

for tipo, resultado in resultados.items():
    print(f'Tipo: {tipo}')
    for tamanho, tempos in resultado.items():
        print(f'Tamanho: {tamanho}')
        for nome, tempo in tempos.items():
            print(f'{nome}: {tempo:.6f} segundos')
        print()

for tipo, resultado in resultados.items():
    plt.figure(figsize=(10, 6))
    for nome in resultado[list(resultado.keys())[0]].keys():
        tempos = [resultado[tamanho][nome] for tamanho in tamanhos]
        plt.plot(tamanhos, tempos, label=nome)
    plt.xlabel('Tamanho da lista')
    plt
