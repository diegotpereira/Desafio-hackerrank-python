# A tarefa do problema "Lonely Integer" no 
# HackerRank envolve a seguinte situação:

# Dada uma lista de números inteiros, todos 
# os números aparecem duas vezes, exceto um 
# número que aparece apenas uma vez. O objetivo 
# é encontrar esse número único que não tem um par na lista.

# Em resumo, o problema "Lonely Integer" requer 
# que você encontre o número inteiro que ocorre 
# apenas uma vez em uma lista onde todos os outros 
# números ocorrem duas vezes. Isso envolve a identificação desse número único.

# from collections import defaultdict

# def lonelyinteger(a):
    
#     # Cria um dicionário com valores padrão inteiros (todos inicializados como 0)
#     b = defaultdict(int)
    
#     # Percorre a lista 'a'
#     for i in a:
        
#         # Incrementa o valor associado à chave 'i' no dicionário 'b'
#         b[i] += 1
        
#     # Retorna a primeira chave (número) no dicionário 'b' cujo valor é igual a 1
#     return list(b.keys())[list(b.values()).index(1)]

# def lonelyinteger(a):
    
#     # Percorre a lista 'a'
#     for i in a:
        
#         # Verifica se o número 'i' ocorre apenas uma vez na lista 'a'
#         if a.count(i) == 1:
            
#             # Se sim, retorna 'i' como o número inteiro solitário
#             return i


def lonelyinteger(a):
    
    # Inicializa o resultado com 0
    resultado = 0
    
    # Percorre a lista 'a'
    for item in a:
        
        # Realiza uma operação de bit XOR entre o resultado atual e o elemento 'item'
        resultado ^= item 
        
    # Se o resultado final for igual a 0, significa que todos os pares se cancelaram,
    # então atribui o primeiro elemento da lista 'a' como resultado
    if resultado == 0:
        
        resultado = a[0]
        
    # Retorna o resultado final, que é o número inteiro solitário
    return resultado