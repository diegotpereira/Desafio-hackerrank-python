# Dado uma string, você precisa determinar o índice de um caractere 
# cuja remoção torne a string um palíndromo. Se a string já for um palíndromo, 
# a função deve retornar -1.

# Um palíndromo é uma sequência de caracteres que é a mesma se lida 
# da esquerda para a direita ou da direita para a esquerda.

# def palindromeIndex(palavra):
    
#     # Verifica se a palavra é um palíndromo 
#     # comparando-a com sua versão invertida.
#     if palavra == palavra[::-1]:
        
#         # Se a palavra já é um palíndromo, 
#         # retorna -1 (nenhum caractere precisa ser removido).
#         return -1
    
#     # Percorre a palavra até a metade do seu comprimento.
#     for i in range(len(palavra) // 2):
        
#         # Verifica se o caractere atual (i-ésimo) é diferente 
#         # do caractere simétrico em relação ao final da palavra.
#         if palavra[i] != palavra[len(palavra) - 1 - i]:
            
#             # Se forem diferentes, tenta remover o caractere na 
#             # posição i e verifica se a nova string é um palíndromo.
#             novaString = palavra[:i] + palavra[i + 1:]
            
#             # Se a nova string (após remover o caractere na posição i) 
#             # for um palíndromo, retorna a posição i.
#             if novaString == novaString[::-1]:
                
#                 return i
            
#             # Caso contrário, tenta remover o caractere no final da palavra (len(palavra) - i - 1) 
#             # e verifica se a nova string é um palíndromo.
#             novaString = palavra[:len(palavra) - i - 1] + palavra[len(palavra) - i:]
            
#             # Se a nova string (após remover o caractere no final da palavra) for um palíndromo, 
#             # retorna a posição len(palavra) - i - 1.
#             if novaString == novaString[::-1]:
                
#                 return len(palavra) - i - 1 
    
#     # Se não for possível tornar a palavra um palíndromo removendo apenas um caractere, retorna -1.
#     return -1

def palindromeIndex(palavra):
    # Função para verificar se a palavra é um palíndromo.
    def is_palindrome(s):
        return s == s[::-1]
    
    # Verifica se a palavra é um palíndromo.
    if is_palindrome(palavra):
        # Se a palavra já é um palíndromo, retorna -1.
        return -1
    
    # Inicializa os ponteiros "baixo" e "alto" para as extremidades da palavra.
    baixo = 0
    alto = len(palavra) - 1
    
    # Enquanto os ponteiros "baixo" e "alto" não se cruzarem.
    while baixo < alto:
        # Se os caracteres nas posições "baixo" e "alto" são diferentes.
        if palavra[baixo] != palavra[alto]:
            # Verifica se a palavra sem o caractere no índice "baixo" é um palíndromo.
            if is_palindrome(palavra[:baixo] + palavra[baixo + 1:]):
                # Se for um palíndromo, retorna o índice "baixo".
                return baixo
            
            # Caso contrário, verifica se a palavra sem o caractere no índice "alto" é um palíndromo.
            if is_palindrome(palavra[:alto] + palavra[alto + 1:]):
                # Se for um palíndromo, retorna o índice "alto".
                return alto
            
            # Se a palavra não for um palíndromo após remover os caracteres em "baixo" ou "alto",
            # significa que é impossível tornar a palavra um palíndromo removendo apenas um caractere.
            return -1
        
        # Move os ponteiros "baixo" para a direita e "alto" para a esquerda.
        baixo += 1
        alto -= 1
    
    # Se o loop terminar sem encontrar caracteres diferentes, a palavra é um palíndromo.
    # Neste caso, a função já teria retornado -1 na primeira verificação.
    return -1
