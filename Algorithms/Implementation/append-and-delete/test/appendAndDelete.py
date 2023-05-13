# A tarefa do problema "Append and Delete" é determinar se 
# é possível transformar uma string inicial em uma string 
# alvo através de operações de anexação (append) e exclusão 
# (delete). Cada operação de anexação adiciona um caractere à 
# string inicial, e cada operação de exclusão remove o último 
# caractere da string inicial. O objetivo é descobrir se é possível 
# realizar um número específico de operações de anexação e exclusão 
# para obter a string alvo a partir da string inicial.


# def appendAndDelete(s, t, k):
    
#     # Definindo as mensagens de resultado
#     positivo = "Yes"
#     negativo = "No"
    
#     # Percorrendo os valores de 1 a k (exclusivo)
#     for i in range(1, k):
        
#         # Verificando se a concatenação de s sem os últimos i caracteres
#         # e t com os últimos (k - i) caracteres é igual a t
#         if s[:-i] + t[-(k - i):] == t:
            
#             # Se for igual, retorna a mensagem positiva
#             return positivo
        
#     # Se nenhum caso for satisfeito, retorna a mensagem negativa
#     return negativo


# def appendAndDelete(stringInicial, stringDesejada, numeroOperacoes):
    
#     # Definindo as mensagens de resultado
#     positivo = "Yes"
#     negativo = "No"
    
#     # Inicializando a variável i com o valor 1
#     i = 1
    
#     # Verificando se a soma dos tamanhos das strings inicial e desejada 
#     # é igual ao número de operações,
#     # ou se as duas strings são iguais
#     if len(stringInicial) + len(stringDesejada) == numeroOperacoes or stringInicial == stringDesejada :
        
#         # Se a condição for satisfeita, retorna a mensagem positiva
#         return positivo
    
#     # Loop while para realizar as operações
#     while i < numeroOperacoes:
        
#         # Removendo o último caractere da string inicial
#         stringInicial = stringInicial[:-1]
        
#         # Verificando se a string inicial é igual aos primeiros caracteres da string desejada
#         # e se o número de operações restantes é igual à diferença entre os tamanhos das strings
#         if stringInicial == stringDesejada[0:len(stringInicial)] and numeroOperacoes - i == len(stringDesejada) - len(stringInicial):
            
#             # Se a condição for satisfeita, retorna a mensagem positiva
#             return positivo
        
#         # Incrementando o valor de i
#         i += 1
        
#     # Se nenhuma condição for satisfeita, retorna a mensagem negativa
#     return negativo
    
    
def appendAndDelete(stringInicial, stringDesejada, numeroOperacoes):
    
    # Definindo as mensagens de resultado
    positivo = "Yes"
    negativo = "No"
    
    # Verifica se o número de operações é igual a 0
    if(numeroOperacoes == 0):
        
        # Verifica se a string inicial é igual à string desejada
        if stringInicial == stringDesejada:
            
            # Retorna "Yes" se forem iguais
            return positivo
        
        else:
            
            # Retorna "No" se forem diferentes
            return negativo
        
    # Verifica se o comprimento da string inicial mais o número 
    # de operações é maior que o comprimento da string desejada
    if len(stringInicial) + numeroOperacoes > len(stringDesejada):
        
        # Chama recursivamente a função, reduzindo a string inicial em 1 caractere 
        # e diminuindo o número de operações em 1
        return appendAndDelete(stringInicial[:-1], stringDesejada, numeroOperacoes - 1)
    
    # Verifica se o comprimento da string inicial mais o número de operações é igual ao 
    # comprimento da string desejada e se a string desejada começa com a string inicial
    if len(stringInicial) + numeroOperacoes == len(stringDesejada) and stringDesejada.startswith(stringInicial):
        
        # Retorna "Yes" se a condição for satisfeita
        return positivo
    
    else:
        
        # Retorna "No" se nenhuma das condições for satisfeita
        return negativo