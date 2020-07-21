from heap_sort import executar as executador_heap_sort
from intro_sort import executar as executador_intro_sort
from merge_sort import executar as executador_merge_sort

if __name__ == '__main__':
    with open("parametros_entrada.txt", "r") as file:
        linha = file.readlines()[0]

        n, metodo = linha.strip().split(",")

        if metodo == "merge_sort":
            executador_merge_sort(int(n))
        elif metodo == "intro_sort":
            executador_intro_sort(int(n))
        elif metodo == "heap_sort":
            executador_heap_sort(int(n))
