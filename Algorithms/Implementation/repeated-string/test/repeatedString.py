# A tarefa do problema "Repeated String" é determinar 
# o número de ocorrências de um caractere específico 
# em uma string repetida até um determinado comprimento. 
# A string é repetida infinitamente e é necessário contar 
# o número de ocorrências do caractere especificado nos 
# primeiros "n" caracteres da string repetida. O objetivo 
# é retornar esse número de ocorrências.

# O link fornecido direciona para o desafio no HackerRank, 
# onde os detalhes completos da tarefa, bem como exemplos 
# de entrada e saída, estão disponíveis.


# def repeatedString(s, n):
    
#     # Conta o número de ocorrências do caractere 'a' na string original
#     resultado = s.count('a')
    
#     # Multiplica o número de ocorrências pelo número de repetições inteiras da string
#     resultado *= n // len(s)
    
#     # Percorre os caracteres restantes da string (caso não seja uma repetição inteira)
#     for index in range(n % len(s)):
        
#         # Verifica se o caractere atual é 'a'
#         if s[index] == 'a':
            
#             # e incrementa o resultado, se for o caso
#             resultado += 1
            
#     # retorna o resultado
#     return resultado

import collections

def repeatedString(s, n):
    
    # Conta as ocorrências de cada caractere na string
    contar_s = collections.Counter(s)
    
    # Obtém a contagem de ocorrências do caractere 'a'
    contar_letra = contar_s['a']
    
    # Calcula quantas vezes 's' se repete em 'n'
    # e multiplica pelo número de ocorrências de 'a'
    numeroRepeticoes = n // len(s) * contar_letra
    
    # Calcula o número de caracteres restantes após repetir 's' em 'n'
    restante = n % len(s)
    
    if restante > 0:
        
        # Verifica os caracteres restantes e conta as ocorrências de 'a'
        for i in range(restante):
            
            if s[i] == 'a':
                
                numeroRepeticoes += 1
                
    # Retorna o total de ocorrências de 'a'
    return numeroRepeticoes 