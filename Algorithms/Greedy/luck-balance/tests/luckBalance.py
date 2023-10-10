# A tarefa do problema "Luck Balance" no 
# HackerRank envolve a seguinte situação:

# Lena está participando de uma competição de 
# programação e ela pode ganhar ou perder certa 
# quantidade de "sorte" dependendo de suas escolhas. 
# A competição consiste em várias rodadas, e em cada 
# rodada, Lena pode escolher participar ou não. Se 
# ela participar, ela ganha ou perde uma quantidade 
# específica de sorte para essa rodada. Se ela não 
# participar, ela não ganha ou perde sorte.

# O objetivo de Lena é maximizar a quantidade de 
# sorte que ela tem no final da competição. No 
# entanto, há uma restrição: Lena só pode perder 
# um número limitado de vezes. Portanto, ela 
# precisa escolher cuidadosamente em quais 
# rodadas participar e em quais não participar 
# para obter a sorte máxima.

# A tarefa específica envolve determinar a 
# quantidade máxima de sorte que Lena pode ter 
# no final da competição, dadas as regras e 
# os valores de sorte associados a cada rodada.

# def luckBalance(k, concursos):
    
#     # Inicialize a variável 'sorte' para 
#     # armazenar o valor da sorte
#     sorte = 0
    
#     # Crie uma lista chamada 'importante' para 
#     # armazenar os concursos importantes
#     importante = []
    
#     # Percorra a lista de concursos
#     for concurso in concursos:
        
#         # Verifique se o concurso não é importante (tem valor 0 de importância)
#         if concurso[1] == 0:
            
#             # Se não for importante, 
#             # adicione o valor da sorte ao total
#             sorte += concurso[0]
            
#         else:
            
#             # Se for importante, 
#             # adicione-o à lista de concursos importantes
#             importante.append(concurso[0])
            
#     # Ordene a lista de concursos importantes em ordem decrescente e itere sobre eles
#     for i, l in enumerate(sorted(importante, reverse=1)):
        
#         # Adicione ou subtraia o valor do concurso importante com base na posição (i) e no valor de (k)
#         sorte += (l * (1 if i < k else -1))
    
#     # Retorne o valor total da sorte
#     return sorte

def luckBalance(k, concursos):
    
    resposta = 0
    w = []
    
    for i in concursos:
        
        if i[i] == 0:
            
            