"""
Implementação do  algortimos Merge Sort em python, feita com base no código de:
    -   Aggarwal, S., Rai, A., Advani, R., Gupta, V., Kushjaing, & Rishiraj. (n.d.). HeapSort - GeeksforGeeks.
        Retrieved July 8, 2020, from https://www.geeksforgeeks.org/heap-sort/
"""


# Python program for implementation of Bubble Sort

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


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


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
        algoritmo = "heap_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "pior"
        tempo = ""
        memoria = ""

        arr = _geracao_pior_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        heap_sort(arr)

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
        algoritmo = "heap_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "medio"

        lista_tempos = []
        lista_memorias = []
        for i in range(5):
            arr = _geracao_casos_medios(tamanho)

            tracemalloc.start()  # definição da contagem de memoria
            start_time = time.time()  # Definição da contagem do tempo

            #  Execução do algortimo
            heap_sort(arr)

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
        algoritmo = "heap_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "melhor"
        tempo = ""
        memoria = ""

        arr = _geracao_melhor_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        heap_sort(arr)

        # Calculo do tempo
        tempo = time.time() - start_time

        #  calculo da memória gasta
        current, peak = tracemalloc.get_traced_memory()
        memoria = peak / 10 ** 6
        tracemalloc.stop()

        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")


def executar(tamanho):
    rodar_melhor(tamanho)
    rodar_medio(tamanho)
    rodar_pior(tamanho)
