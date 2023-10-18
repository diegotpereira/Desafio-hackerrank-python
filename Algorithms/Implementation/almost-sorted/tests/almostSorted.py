# O problema "Almost Sorted" pede 
# para você determinar se é possível 
# transformar um array de números em 
# ordem crescente ao realizar uma única 
# operação de swap (troca) ou, se não 
# for possível, determinar se é possível 
# ordenar uma subseção contígua do array 
# para que o array inteiro seja ordenado 
# em ordem crescente.

# A entrada para o problema consiste 
# em um array de inteiros. Sua tarefa é 
# verificar se é possível realizar uma 
# única operação de swap em dois elementos 
# do array para torná-lo completamente 
# ordenado ou, se não for possível, 
# determinar se é possível ordenar uma 
# seção contígua do array para que o 
# array inteiro seja ordenado em ordem crescente.

# A saída deve indicar se é possível realizar 
# a operação de swap, se é possível ordenar 
# uma seção contígua ou se é impossível 
# realizar qualquer uma das duas operações.

# def almostSorted(arr):
    
#     # Cria uma cópia ordenada do array de entrada
#     arr_ordenado = sorted(arr)
    
#     # Encontra as diferenças entre os elementos do array original e o array ordenado
#     diferenca = [(i, a) for i, (a, b) in enumerate(zip(arr, arr_ordenado)) if a != b]
    
#     # Verifica se é possível realizar uma troca para ordenar o array
#     if len(diferenca) == 2 and arr[diferenca[0][0]] == arr_ordenado[diferenca[1][0]] and arr[diferenca[1][0]] == arr_ordenado[diferenca[0][0]]:
        
#         # Imprime 'yes' para indicar que a ordenação é possível
#         return('yes') 
        
#         # Imprime os índices dos elementos a serem trocados
#         return('swap', diferenca[0][0] + 1, diferenca[1][0] + 1)
        
#     else:
        
#         # Caso a troca não seja possível, encontra a subsequência reversa que, se ordenada, corrigiria o array
#         sub_lista_reversa = arr[diferenca[0][0] : diferenca[-1][0] + 1][::-1]
        
#         # Verifica se a subsequência reversa é igual à subsequência correspondente no array ordenado
#         if sub_lista_reversa == arr_ordenado[diferenca[0][0] : diferenca[-1][0] + 1]:
            
#             # Imprime 'yes' para indicar que a ordenação é possível
#             return('yes')
        
#             # Imprime os índices da subsequência a ser invertida
#             return('reverse', diferenca[0][0] + 1, diferenca[-1][0] + 1)
            
#         else:
            
#             # Imprime 'no' para indicar que a ordenação não é possível
#             return('no')
    
def almostSorted(arr):
    
    # Ordena o array de entrada e armazena o resultado em "array"
    array = sorted(arr)
    
    # Inicializa uma lista vazia chamada "resposta" para armazenar índices de elementos fora de ordem
    resposta = []
    
    # Percorre os elementos de "arr" e "array" ao mesmo tempo, mantendo o índice "i"
    for i, (array, b) in enumerate(zip(arr, array)):
        
        # Verifica se o elemento de "arr" não é igual ao elemento correspondente em "array"
        if array != b:
            
            # Se forem diferentes, adiciona o índice "i" à lista "resposta"
            resposta.append(i)
        
    # Se não houver elementos fora de ordem, o array já está ordenado
    if len(resposta) == 0:
        
        # Retorna 'yes' para indicar que o array está ordenado
        return 'yes'
    
    # Se houver exatamente 2 elementos fora de ordem, é possível fazer uma troca para ordená-los
    elif len(resposta) == 2:
        
        # Retorna 'yes' e imprime uma mensagem com os índices dos elementos a serem trocados
        print('swap', + '' + str(resposta[0] + 1) + '' + str(resposta[1] + 1))
        return 'yes'
        
    # Se houver mais de 2 elementos fora de ordem, verifica se é possível reverter uma subsequência
    elif len(resposta) > 2:
        
        for j in range(1, len(resposta)):
            
            # Se houver um elemento fora de ordem entre dois elementos consecutivos, o array não pode ser ordenado
            if arr[resposta[j - 1]] < arr[resposta[j]]:
                
                return 'no'
        
        # Se for possível reverter uma subsequência, retorna 'yes' e imprime uma mensagem com os índices da subsequência a ser invertida
        print('reverse', + '' + str(resposta[0] + 1) + '' + str(resposta[-1] + 1))
        return 'yes'
    
    else:
        
        # Se nenhuma das condições anteriores for atendida, o array não pode ser ordenado
        return 'no'