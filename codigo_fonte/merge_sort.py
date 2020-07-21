"""
Implementação do  algortimos Merge Sort em python, feita com base no código de:
    -   chitranayal & Mayank Khanna 2. (2016). Merge Sort - GeeksforGeeks.
        Retrieved July 4, 2020, from https://www.geeksforgeeks.org/merge-sort/?ref=rp
"""


import random
import time
import tracemalloc
from datetime import datetime


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def _geracao_melhor_caso(qtd):
    """
    Gera o melhor caso do merge. Uma lista ordenada
    :param qtd:
    :return: list
    """
    return list(range(qtd))


def _geracao_pior_caso(qtd):
    """
    Gera o pior caso do merge. Neste caso o merge irá fazer o maior numero de comparaçõe possiveis
    :param qtd:
    :return: list
    """
    random_list = list(range(qtd))
    for i in range(0, len(random_list), 2):
        random_list[i] = len(random_list) + i
    return random_list


def _geracao_casos_medios(qtd):
    randomlist = random.sample(range(0, qtd), qtd)

    return randomlist


def rodar_pior(tamanho):

    print("Rodando pior caso")
    with open("resultados.csv", "a+") as file:
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        algoritmo = "merge_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "pior"
        tempo = ""
        memoria = ""

        arr = _geracao_pior_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        mergeSort(arr)

        # Calculo do tempo
        tempo = time.time() - start_time

        #  calculo da memória gasta
        current, peak = tracemalloc.get_traced_memory()
        memoria = peak / 10 ** 6
        tracemalloc.stop()

        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")


def rodar_medio(tamanho):

    print("Rodando caso medio")
    with open("resultados.csv", "a+") as file:
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        algoritmo = "merge_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "medio"

        lista_tempos = []
        lista_memorias = []
        for i in range(5):
            arr = _geracao_casos_medios(tamanho)

            tracemalloc.start()  # definição da contagem de memoria
            start_time = time.time()  # Definição da contagem do tempo

            #  Execução do algortimo
            mergeSort(arr)

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
        algoritmo = "merge_sort"
        tamanho_para_salvar = f"{tamanho}"
        caso = "melhor"
        tempo = ""
        memoria = ""

        arr = _geracao_melhor_caso(tamanho)

        tracemalloc.start()  # definição da contagem de memoria
        start_time = time.time()  # Definição da contagem do tempo

        #  Execução do algortimo
        mergeSort(arr)

        # Calculo do tempo
        tempo = time.time() - start_time

        #  calculo da memória gasta
        current, peak = tracemalloc.get_traced_memory()
        memoria = peak / 10 ** 6
        tracemalloc.stop()

        # Escreve arquivo
        file.write(f"{hora_inicio},{algoritmo},{tamanho_para_salvar},{caso},{tempo},{memoria}\n")

def executar(tamanho):
    import sys

    sys.setrecursionlimit(10000000)

    rodar_melhor(tamanho)
    rodar_medio(tamanho)
    rodar_pior(tamanho)
