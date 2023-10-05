# Dado um conjunto de pacotes 
# de doces com valores diferentes 
# e um número inteiro K, a tarefa 
# é determinar a diferença mínima 
# entre os valores dos pacotes 
# que serão escolhidos por K crianças.

# Detalhes da Tarefa:

# Você recebe um array de inteiros 
# que representa o valor de cada 
# pacote de doces.
# O objetivo é dividir os pacotes 
# entre K crianças de tal forma 
# que a diferença entre os 
# valores dos pacotes escolhidos 
# por cada criança seja minimizada.
# Cada criança recebe exatamente 
# um pacote.
# O número de pacotes é sempre maior ou igual a K.
# Exemplo:

# Por exemplo, suponha que você tenha os
# seguintes valores de pacotes de doces: [10, 100, 300, 200, 1000, 20, 30]. 
# Se você deseja dividir esses pacotes entre 3 crianças (K = 3), 
# uma maneira de minimizar a diferença é escolher os pacotes [30, 100, 200] 
# para a primeira criança, [10, 20, 300] para a segunda criança e [1000] 
# para a terceira criança. Nesse caso, a diferença mínima entre os valores 
# dos pacotes é 40 (1000 - 960).

# A tarefa consiste em escrever um programa que calcule essa diferença 
# mínima entre os valores dos pacotes escolhidos pelas K crianças.

# Para a implementação completa e detalhes específicos sobre as entradas 
# e saídas esperadas, você deve acessar o link fornecido no HackerRank 
# que você mencionou inicialmente. Lá, você encontrará exemplos de 
# entrada/saída e poderá enviar sua solução para verificar se está correta.


# # Importa o módulo 'sys' para usar 'sys.maxsize'.
# import sys

# # Define a função 'maxMin' que 
# # recebe como entrada um número 'k' e uma lista 'arr'
# def maxMin(k, arr):
    
#     # Ordena a lista 'arr' em ordem crescente
#     arr.sort()
    
#     # Inicializa a variável 'injustiça' 
#     # com um valor muito grande, 
#     # equivalente ao valor máximo em seu sistema
#     injustiça = sys.maxsize
    
#     # Loop que percorre a lista 'arr' com base no valor de 'k'
#     for i in range(len(arr) - k + 1):
        
#         # Calcula a diferença entre o elemento no 
#         # índice 'i + k - 1' e o elemento no índice 'i'.
#         if arr[i + k - 1] - arr[i] < injustiça:
            
#             # Se a diferença calculada for menor que a 
#             # 'injustiça' atual, atualiza 'injustiça'
#             injustiça = arr[i + k - 1] - arr[i]
    
#     # Retorna o valor mínimo de injustiça encontrado
#     return injustiça

# Define a função 'maxMin' que recebe 
# como entrada um número 'k' e uma lista 'arr'

# def maxMin(k, arr):
    
#     # Ordena a lista 'arr' em ordem crescente
#     arr.sort()
    
#     # Inicializa os índices 'i' e 'j' para criar uma janela de tamanho 'k
#     i = 0
    
#     # último elemento dessa janela
#     j = k - 1
    
#     # Inicializa 'm' com o maior valor possível, 
#     # que é o último elemento da lista após a ordenação
#     m = arr[-1]
    
#     # Enquanto 'j' não ultrapassar o comprimento da lista
#     while j < len(arr):
        
#         # Calcula a diferença entre o 
#         # elemento no índice 'j' e o elemento no índice 'i'
#         diferenca = arr[j] - arr[i]
        
#         # Atualiza 'm' com o valor mínimo entre 'm' 
#         # atual e a diferença calculada
#         m = min(m, diferenca)
        
#         # Incrementa 'i' e 'j' para mover a janela
#         i += 1
#         j += 1
        
#     # Retorna o valor mínimo de diferença encontrado na janela
#     return m


# # Define a função 'maxMin' que recebe 
# # como entrada um número 'k' e uma lista 'arr'
# def maxMin(k, arr):
    
#     # Ordena a lista 'arr' em ordem crescente
#     arr.sort()
    
#     #  Calcula a diferença mínima entre os elementos adjacentes em uma janela de tamanho 'k'.
#     # O loop abrange índices de 'k - 1' até o último elemento da lista.
#     # A diferença entre os elementos adjacentes é calculada e o valor mínimo é retornado.
#     return min(arr[i] - arr[i - k + 1] for i in range(k -1, len(arr)))


# Define a função 'maxMin' que recebe como entrada um número 'k' e uma lista 'arr'.

def maxMin(k, arr):
    
    # Ordena a lista 'arr' em ordem crescente
    arr = sorted(arr)
    
    # Calcula a diferença entre o maior 
    # e o menor elemento da lista após a ordenação
    diferenca = arr[-1] - arr[0]
    
    # Loop que percorre a lista 'arr' para calcular a diferença mínima entre elementos adjacentes em uma janela de tamanho 'k'
    for i in range(0, len(arr) - k + 1):
        
        # Calcula a diferença entre o elemento no 
        # índice 'i + k - 1' e o elemento no índice 'i'
        tmp = arr[i + k - 1] - arr[i]
        
        # Se a diferença calculada for menor que a diferença atual, 
        # atualiza 'diferenca'
        if tmp < diferenca:
            
            diferenca = tmp 
            
    # Retorna a diferença mínima encontrada
    return diferenca