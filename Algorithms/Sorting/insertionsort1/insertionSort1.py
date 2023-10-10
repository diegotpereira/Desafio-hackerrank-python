# A tarefa do problema "Insertion Sort - Part 1" no HackerRank
# é implementar a primeira etapa do algoritmo de ordenação por 
# inserção (insertion sort). Nessa etapa, você deve realizar uma 
# única iteração do algoritmo para "inserir" um elemento em sua 
# posição correta dentro de uma lista ordenada.

# A entrada do problema consiste em duas partes:

# Um número inteiro, que representa o tamanho da lista de elementos.
# Uma lista de números inteiros separados por espaços, que representam os 
# elementos da lista.
# A saída esperada é a lista após uma iteração do algoritmo de ordenação 
# por inserção. Durante a iteração, você deve mover um elemento da lista 
# para sua posição correta de acordo com a ordem crescente. Você deve 
# imprimir a lista após essa única iteração.

# A ideia básica do algoritmo de ordenação por inserção é que ele começa
# com uma lista de um único elemento (o primeiro elemento da entrada) e, 
# em seguida, insere cada elemento subsequente na posição correta na parte 
# já ordenada da lista. A cada iteração, um novo elemento é inserido na 
# posição correta, expandindo a parte ordenada da lista.


def insertionSort1(n, arr):

    # Inicializa ultimo_elemento_lista com o último elemento da lista.
    ultimo_elemento_lista = arr[n - 1]

    # Loop que itera da penúltima posição até a primeira posição da lista.
    for i in range(n - 1, -1, -1):

        if arr[i - 1] > arr[i]:

            arr[i] = arr[i - 1]

            print(*arr)

            arr[i - 1] = ultimo_elemento_lista

            if arr == sorted(arr):

                print(*arr)
                break

        else:

            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            print(*arr)

            if arr == sorted(arr):

                break