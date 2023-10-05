# A tarefa do problema "Modified Kaprekar Numbers" no 
# HackerRank é determinar e imprimir os números de Kaprekar 
# modificados em um determinado intervalo. Os números de 
# Kaprekar têm a propriedade especial de que, quando o 
# quadrado do número é dividido em duas partes, essas 
# partes somadas resultam no número original.

# A tarefa exige que você implemente uma função chamada 
# kaprekarNumbers, que recebe dois argumentos, p e q, 
# que são os limites do intervalo que você deve verificar. 
# A função deve imprimir todos os números de Kaprekar 
# nesse intervalo.

# O formato de saída esperado é uma série de números 
# separados por espaços. Se não houver números de Kaprekar 
# no intervalo, a função deve imprimir a mensagem "INVALID RANGE".

# def kaprekarNumbers(limite_superior, limite_inferior):
    
#     # Inicializando uma lista para armazenar os números de Kaprekar encontrados
#     numeros_kaprekar = []
    
#     # Iterando por todos os números no intervalo [limite_superior, limite_inferior]
#     for num in range(limite_superior, limite_inferior + 1):
        
#         # Calculando o tamanho do número atual convertido em string
#         tamanho_num = len(str(num))
        
#         # Calculando o quadrado do número atual
#         quadrado = num * num
        
#         # Convertendo o quadrado em uma string para análise
#         string_quadrado = str(quadrado)
        
#         # Extraindo a parte direita do quadrado
#         direita = string_quadrado[-tamanho_num:]
        
#         # Extraindo a parte esquerda do quadrado
#         esquerda = string_quadrado[:len(string_quadrado) - tamanho_num]
        
#         # Convertendo as partes em números inteiros, 
#         # tratando o caso em que uma parte pode estar vazia
#         esquerda = int(esquerda) if esquerda != "" else 0
#         direita = int(direita) if direita != "" else 0
        
#         # Verificando se a soma das partes direita e esquerda é igual ao número original
#         if direita + esquerda == num:
            
#             # Se for um número de Kaprekar, adicioná-lo à lista
#             numeros_kaprekar.append(str(num))
    
#     # Retornando a lista de números de Kaprekar encontrados
#     if len(numeros_kaprekar) == 0:
        
#         return ('INVALID RANGE')
    
#     return (' '.join(numeros_kaprekar))


def kaprekarNumbers(limite_superior, limite_inferior):
    
    # Inicialização da variável para 
    # verificar se números foram encontrados
    encontrado = False
    
    # Inicialização da string para armazenar 
    # os números encontrados
    resultado = ""
    
    # Loop através dos números no intervalo especificado
    for num in range(limite_superior, limite_inferior + 1):
        
        # Calculando o quadrado do número e convertendo em string
        numero = str(num * num)
        
        # Obtendo os dígitos da esquerda e direita do número
        esquerda = numero[:-len(str(num))]
        direita = numero[-len(str(num)):]
        
        # Verificando se a soma das partes esquerda 
        # e direita é igual ao número original
        if int(esquerda or 0) + int(direita) == num:
            
            # Marcando que pelo menos 
            # um número foi encontrado
            encontrado = True 
            
            # Adicionando o número encontrado 
            # à string de resultado
            resultado += str(num) + " "
            
    # Verificando se números foram encontrados ou não
    if not encontrado:
        
        # Caso nenhum número tenha sido encontrado, 
        # retorna uma mensagem de erro
        return "INVALID RANGE"
    
    # Removendo espaços em branco extras 
    # e retornando os números encontrados
    return resultado.strip()




