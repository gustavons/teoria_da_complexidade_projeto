"""
Implementação do  algoritmo Intro Sort em python, feita com base no código de:
    - Karthikeyan, L. (n.d.). IntroSort or Introspective sort - GeeksforGeeks.
        Retrieved from https://www.geeksforgeeks.org/introsort-or-introspective-sort/
    -  Aggarwal, S., Rai, A., Advani, R., Gupta, V., Kushjaing, & Rishiraj. (n.d.). HeapSort - GeeksforGeeks.
        Retrieved July 8, 2020, from https://www.geeksforgeeks.org/heap-sort/
"""


# Python program for implementation of Bubble Sort
import math
import random
import threading
import time
import tracemalloc
from datetime import datetime

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def Partition(arr, low, high):

    # pivot

    pivot = arr[high]

    # index of smaller element

    i = low - 1

    for j in range(low, high):

        # If the current element is smaller than or
        # equal to the pivot

        if arr[j] <= pivot:
            # increment index of smaller element

            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


# The function to find the median
# of the three elements in
# in the index a, b, d


def MedianOfThree(arr, a, b, d):
    A = arr[a]
    B = arr[b]
    C = arr[d]

    if A <= B and B <= C:
        return b
    if C <= B and B <= A:
        return b
    if B <= A and A <= C:
        return a
    if C <= A and A <= B:
        return a
    if B <= C and C <= A:
        return d
    if A <= C and C <= B:
        return d

    # The main function that implements Introsort


# The main function to sort the data using
# insertion sort algorithm


def InsertionSort(arr, begin, end):
    left = begin
    right = end

    # Traverse through 1 to len(arr)

    for i in range(left + 1, right + 1):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def IntrosortUtil(arr, begin, end, depthLimit):
    size = end - begin
    if size < 16:
        # if the data set is small, call insertion sort

        InsertionSort(arr, begin, end)
        return

    if depthLimit == 0:
        # if the recursion limit is occurred call heap sort

        heapSort(arr)
        return

    pivot = MedianOfThree(arr, begin, begin + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])

    # partitionPoint is partitioning index,
    # arr[partitionPoint] is now at right place
    partitionPoint = Partition(arr, begin, end)

    # Separately sort elements before partition and after partition

    IntrosortUtil(arr, begin, partitionPoint - 1, depthLimit - 1)
    IntrosortUtil(arr, partitionPoint + 1, end, depthLimit - 1)


# A utility function to begin the Introsort module


def Introsort(arr):
    begin = 0
    end = len(arr) - 1
    # initialise the depthLimit as 2 * log(length(data))

    depthLimit = 2 * math.log2(end - begin)
    IntrosortUtil(arr, begin, end, depthLimit)


def _geracao_pior_caso(qtd):
    return list(range(qtd))


def _geracao_melhor_caso(qtd):
    random_list = list(range(qtd))
    random_list.reverse()
    return random_list


def _geracao_casos_medios(qtd):
    randomlist = random.sample(range(0, qtd), qtd)

    return randomlist


def rodar_pior(tamanho):
    print("Rodando pior caso")
    with open("resultados.csv", "a+") as file:
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        algoritmo = "intro_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "pior"
        tempo = ""
        memoria = ""

        arr = _geracao_pior_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        Introsort(arr)

        # Calculo do tempo
        tempo = time.time() - start_time

        #  calculo da memória gasta
        current, peak = tracemalloc.get_traced_memory()
        memoria = peak / 10 ** 6
        tracemalloc.stop()

        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")


def rodar_medio(tamanho):
    print("Rodando medio caso")
    with open("resultados.csv", "a+") as file:
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        algoritmo = "intro_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "medio"

        lista_tempos = []
        lista_memorias = []
        for i in range(5):
            arr = _geracao_casos_medios(tamanho)

            tracemalloc.start()  # definição da contagem de memoria
            start_time = time.time()  # Definição da contagem do tempo

            #  Execução do algortimo
            Introsort(arr)

            # Calculo do tempo
            lista_tempos.append(time.time() - start_time)

            #  calculo da memória gasta
            current, peak = tracemalloc.get_traced_memory()
            lista_memorias.append(peak / 10 ** 6)
            tracemalloc.stop()

        memoria = sum(lista_memorias) / len(lista_memorias)
        tempo = sum(lista_tempos) / len(lista_tempos)
        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")


def rodar_melhor(tamanho):
    print("Rodando Melhor caso")
    with open("resultados.csv", "a+") as file:
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        algoritmo = "intro_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "melhor"
        tempo = ""
        memoria = ""

        arr = _geracao_melhor_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        Introsort(arr)

        # Calculo do tempo
        tempo = time.time() - start_time

        #  calculo da memória gasta
        current, peak = tracemalloc.get_traced_memory()
        memoria = peak / 10 ** 6
        tracemalloc.stop()

        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")


def roda(caso):
    tamanhos = [100, 1000, 10000, 100000, 1000000, 10000000]
    if caso == "melhor":
        for tamanho in tamanhos:
            rodar_melhor(tamanho)

    elif caso == "medio":
        for tamanho in tamanhos:
            rodar_medio(tamanho)

    elif caso == "pior":

        for tamanho in tamanhos:
            rodar_pior(tamanho)


def executar(tamanho):
    import sys

    sys.setrecursionlimit(10000000)

    rodar_melhor(tamanho)
    rodar_medio(tamanho)
    rodar_pior(tamanho)
