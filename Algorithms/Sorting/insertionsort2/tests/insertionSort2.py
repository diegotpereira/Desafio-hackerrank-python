# A tarefa do problema "Insertion Sort - Part 2" no HackerRank é implementar o algoritmo de ordenação por inserção (Insertion Sort) para ordenar um array de inteiros em várias etapas, onde você é solicitado a imprimir o array após cada etapa da ordenação.

# Aqui está um resumo da tarefa:

# Você recebe um array de inteiros não ordenados.
# Sua tarefa é implementar o algoritmo de ordenação por inserção para ordenar o array em ordem crescente.
# Após cada etapa da ordenação (ou seja, após inserir cada elemento em sua posição correta), você deve imprimir o array atualizado.

def insertionSort2(n, arr):
    
    # Inicialize uma lista vazia chamada 'resultados' 
    # para armazenar o estado do array após cada iteração
    resultados = []
    
    # Percorra o array a partir do segundo elemento (índice 1)
    for i in range(1, len(arr)):
        
        # Armazena o valor do elemento atual em 'chave_valor'
        chave_valor = arr[i]
        
        # Inicialize 'j' como o índice anterior ao elemento atual
        j = i - 1
        
        # Continue movendo elementos maiores à direita do 
        # array até encontrar a posição correta para 'chave_valor'
        while arr[j] > chave_valor and j >= 0:
            
            # Move o elemento à direita
            arr[j + 1] = arr[j]
            
            # Atualiza 'j' para verificar o próximo elemento à esquerda
            j -= 1
            
            # Insere 'chave_valor' na posição correta
            arr[j + 1] = chave_valor
        
        # Crie uma cópia do array após cada iteração e adicione-a à lista 'resultados'
        resultados.append(arr.copy())

    # Retorne a lista 'resultados' contendo o estado do array após cada iteração
    return resultados
