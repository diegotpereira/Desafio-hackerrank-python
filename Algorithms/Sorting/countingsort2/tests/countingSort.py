# A tarefa do problema "Counting Sort 2" no HackerRank 
# é implementar o algoritmo de ordenação chamado "Counting Sort" 
# para ordenar um array de inteiros em ordem não decrescente. 
# O Counting Sort é um algoritmo de ordenação eficiente quando 
# os elementos do array têm valores em um intervalo conhecido e pequeno.

# Aqui está um resumo da tarefa:

# Você recebe um array de inteiros não ordenados.
# Sua tarefa é ordenar o array em ordem não decrescente 
# usando o algoritmo Counting Sort.
# Você deve retornar o array ordenado.

# def countingSort(arr):
    
#     # Classifique o array 'arr' em ordem crescente
#     arr.sort()
    
#     # Retorne o array ordenado
#     return arr

def countingSort(arr):
    
    # Inicialize uma lista vazia chamada 'resposta' 
    # para armazenar o array ordenado
    resposta = []
    
    # Inicialize uma lista chamada 'resultado' com 100 
    # elementos inicializados com zero para contar as ocorrências de cada elemento
    resultado = [0] * 100
    
    # Percorra os elementos do array 'arr'
    for i in arr: 
        
        # Incremente o valor no índice correspondente 
        # em 'resultado' para contar a frequência de ocorrência de 'i'
        resultado[i] += 1
        
    # Percorra os índices em 'resultado'
    for i in range(len(resultado)):
        
        # Adicione 'i' repetidas vezes (com base no valor em 'resultado[i]') 
        # à lista 'resposta' para criar o array ordenado
        resposta += [i] * resultado[i]
        
    # Retorne a lista 'resposta', que contém o array ordenado
    return resposta