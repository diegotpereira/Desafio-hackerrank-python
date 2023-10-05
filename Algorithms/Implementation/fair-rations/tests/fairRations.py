# Dado um array de inteiros 
# que representa a quantidade 
# de pães que cada pessoa tem, 
# você precisa distribuir pães 
# adicionais de forma que cada 
# pessoa tenha uma quantidade 
# par de pães. No entanto, 
# você só pode distribuir os 
# pães adicionais entre pessoas 
# adjacentes, ou seja, entre 
# duas pessoas consecutivas 
# no array. O objetivo é determinar 
# o número mínimo de pães 
# adicionais que precisam ser 
# distribuídos para que todas 
# as pessoas tenham uma quantidade 
# par de pães.

# O problema geralmente fornece a 
# quantidade de pães que cada pessoa 
# já possui em um array e pede que 
# você calcule o número mínimo de 
# distribuições necessárias. A saída 
# esperada é o número mínimo de pães 
# adicionais a serem distribuídos ou,
# se não for possível fazer todas as 
# quantidades de pães ficarem pares, 
# a saída deve ser "NO".

# Definindo a função para verificar se um número é estranho (ímpar)
def ehEstranho(i):
    
    return i % 2 == 1

# Definindo a função principal fairRations que resolve o problema
# def fairRations(B):
    
#     # Contando quantos números ímpares estão presentes na lista B
#     chances = sum([1 for num in B if ehEstranho(num)])
    
#     # Se o número de chances for ímpar, 
#     # não é possível fazer uma distribuição justa
#     if ehEstranho(chances):
        
#         return 'NO'
    
#     # Inicializando a contagem de pães adicionais
#     c = 0
    
#     # Obtendo o tamanho da lista B
#     n = len(B)
    
#     # Percorrendo a lista B, 
#     # exceto o último elemento
#     for i in range(n - 1):
        
#         # Verificando se o número é ímpar
#         if ehEstranho(B[i]):
            
#             # Incrementando o número atual 
#             B[i] += 1
            
#             # Incrementando próximo número da lista
#             B[i + 1] += 1
            
#             # Incrementando a contagem de pães adicionais em 2
#             c += 2
        
    
#     # Convertendo a contagem para uma string e retornando
#     return str(c)

# def fairRations(B):
    
#     # Inicializa um contador para registrar o número de operações
#     contador = 0
    
#     # Loop que percorre os elementos da lista B
#     for i in range(len(B)):
        
#         # Início de um bloco try-except para 
#         # lidar com possíveis exceções
#         try: 
            
#             # Verifica se o elemento atual é ímpar
#             if B[i] % 2 is 1:
                
#                 # Incrementa o contador em 2, 
#                 # já que dois pães serão distribuídos
#                 contador += 2
                
#                 # Incrementa o próximo elemento da 
#                 # lista para equilibrar a distribuição
#                 B[i + 1] += 1
               
#         # Bloco que captura exceções 
#         except:
            
#             # Se ocorrer uma exceção, 
#             # a função retorna 'NO'
#             return 'NO'
    
#     # Retorna o contador convertido para 
#     # string como resultado da função
#     return str(contador)


# # Função que tenta realizar uma distribuição justa de pães entre pessoas
# def fairRations(B):
    
#     # Par = 0, ímpar = 1
    
#     # Convertendo os valores da lista em valores 0 para pares e 1 para ímpares
#     B = [bi % 2 for bi in B]
    
#     # variavel para tamanho de B
#     N = len(B)
    
#      # Inicializa um contador para registrar o número de operações
#     contador = 0
    
#     # Loop que percorre a lista até o penúltimo elemento
#     for i in range(N - 1):
        
#         # Se o elemento atual for ímpar
#         if B[i] == 1:
            
#             # Torna o elemento atual par, 
#             # adicionando 1 e usando o operador % para alternar entre 0 e 1
#             B[i] = (B[i] + 1) % 2
            
#             # Torna o próximo elemento par da mesma forma
#             B[i + 1] = (B[i + 1] + 1) % 2
            
#             # Incrementa o contador em 2, 
#             # já que dois pães serão distribuídos
#             contador += 2
            
#         # Se houver exatamente uma pessoa ímpar na lista
#         if sum(B) == 1:
            
#             # Retorna 'NO', 
#             # indicando que não é possível fazer uma distribuição justa
#             return 'NO'
        
#         # Se todos os elementos da lista forem pares
#         if sum(B) == 0:
            
#             # Retorna o contador convertido para string como resultado da função
#             return str(contador)


# Função para tentar realizar uma distribuição justa de pães entre pessoas
# def fairRations(B):
    
#     # Se a soma dos elementos da lista B for ímpar
#     if sum(B) % 2 != 0:
        
#         # Retorna 'NO', 
#         # indicando que uma distribuição justa não é possível
#         return 'NO'
    
#     # Inicializa um contador para registrar o número de operações
#     contador = 0
    
#     # Loop que percorre os elementos da lista B
#     for i in range(0, len(B)):
        
#         # Se o elemento atual for ímpar
#         if B[i] % 2 != 0:
            
#             # Incrementa o próximo elemento da lista para torná-lo par
#             B[i + 1] += 1
            
#             # Incrementa o contador em 2, já que dois pães serão distribuídos
#             contador += 2
            
#     # Retorna o contador convertido para string como resultado da função
#     return str(contador)


# Função que tenta realizar uma distribuição justa de pães entre pessoas
def fairRations(B):
    
     # Lista para armazenar os índices dos elementos ímpares na lista B
    impar_indice = []
    
    # Loop que percorre os elementos da lista B
    for i in range(len(B)):
        
        # Se o elemento atual for ímpar
        if B[i] % 2 == 1:
            
            # Adiciona o índice do elemento ímpar à lista impar_indice
            impar_indice.append(i)
            
    # Se a quantidade de elementos ímpares for ímpar
    if len(impar_indice) % 2 == 1:
        
        # Retorna 'NO', 
        # indicando que uma distribuição justa não é possível
        return 'NO'
    
    # Variável para armazenar o número total de pães a serem distribuídos
    numeros_de_paes = 0
    
    # Loop que percorre os índices dos elementos ímpares em pares
    for j in range(0, len(impar_indice) - 1, 2):
        
        # Calcula o número de pães a serem distribuídos entre os pares de elementos ímpares
        numeros_de_paes += 2 * abs(impar_indice[j] - impar_indice[j + 1])
        
    # Retorna o total de pães a serem distribuídos convertido para string como resultado da função
    return str(numeros_de_paes)