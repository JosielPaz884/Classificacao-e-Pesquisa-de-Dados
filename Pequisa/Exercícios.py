import random
import time
import math

#1a)
def buscaBinariaIterativa(arr, x):
    esquerda, direita = 0, len(arr) - 1
    
    while esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2
        
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
            
    return -1
  
#1b)
def buscaBinariaRecursiva(arr, x, esquerda, direita):
    if direita >= esquerda:
        meio = esquerda + (direita - esquerda) // 2
        
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            return busca_binaria_recursiva(arr, x, meio + 1, direita)
        else:
            return busca_binaria_recursiva(arr, x, esquerda, meio - 1)
    
    return -1


#2a)
def pesquisaPorSalto(arr, x):
    n = len(arr)
    salto = int(math.sqrt(n))
    prev = 0
    
    while arr[min(salto, n) - 1] < x:
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < x:
        prev += 1
        if prev == min(salto, n):
            return -1
            
    if arr[prev] == x:
        return prev
    
    return -1
  
#2b)
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def pesquisaFibonacci(arr, x):
    n = len(arr)
    fib = fibonacci(n)
    
    offset = -1
    
    for i in range(len(fib) - 1, 0, -1):
        if fib[i] > n:
            continue
        if arr[min(offset + fib[i - 2], n - 1)] < x:
            offset = offset + fib[i - 2]
        elif arr[min(offset + fib[i - 2], n - 1)] > x:
            continue
        else:
            return min(offset + fib[i - 2], n - 1)
    
    if offset + 1 < n and arr[offset + 1] == x:
        return offset + 1
    
    return -1


#3)
arr = sorted(random.sample(range(1, 100000), 10000))
x = random.choice(arr)  
start = time.time()
busca_binaria_iterativa(arr, x)
end = time.time()
print(f"Busca Binária Iterativa: {end - start:.6f} segundos")
start = time.time()
busca_binaria_recursiva(arr, x, 0, len(arr) - 1)
end = time.time()
print(f"Busca Binária Recursiva: {end - start:.6f} segundos")
start = time.time()
pesquisa_por_salto(arr, x)
end = time.time()
print(f"Pesquisa por Salto: {end - start:.6f} segundos")
start = time.time()
pesquisa_fibonacci(arr, x)
end = time.time()
print(f"Pesquisa Fibonacci: {end - start:.6f} segundos")

#a. Qual método teve o menor número de comparações em média?
#Em média, a busca binária (iterativa e recursiva) tende a ter o menor número de comparações, 
#pois tem uma complexidade de O(log n). A pesquisa por salto e a pesquisa Fibonacci têm complexidades semelhantes, 
#mas a pesquisa por salto pode ter um desempenho ligeiramente inferior em alguns casos, dependendo do tamanho do salto escolhido.

#b. Em quais situações você acha que cada método seria mais apropriado?
#A busca binária é mais apropriada quando a lista está ordenada e você precisa encontrar um elemento específico rapidamente. 
#A pesquisa por salto é mais apropriada quando você precisa encontrar um elemento em uma lista muito grande e ordenada, 
#mas não precisa encontrar o elemento exato. A pesquisa Fibonacci é mais apropriada quando você precisa encontrar um 
#elemento em uma lista muito grande e ordenada, e o tamanho da lista é desconhecido.

#c. Como a ordenação da lista afeta a eficiência de cada método?
#A ordenação da lista é essencial para a eficiência de todos os métodos. 
#Se a lista não estiver ordenada, a busca binária, a pesquisa por salto e a 
#pesquisa Fibonacci não funcionarão corretamente. Além disso, a ordenação da lista 
#também pode afetar a eficiência da pesquisa por salto e da pesquisa Fibonacci, pois 
#elas dependem do tamanho do salto e do tamanho da lista, respectivamente.
