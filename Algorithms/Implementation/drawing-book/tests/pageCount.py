# n número total de páginas do livro
# p número da página que o leitor deseja chegar

# def pageCount(n, p):

    
#     # Verifica se p é par
#     if p % 2 == 0:
        
#         # Se p é par, retorna o mínimo entre p//2 e n//2 - p//2
#         return min(p//2, n//2 - p//2)
#     else :
        
#         # Se p é ímpar, retorna o mínimo entre (p - 1)//2, (n - 1)//2 - (p - 1)//2 + 1
#         return min((p - 1)// 2, (n - 1)//2 - (p - 1)// 2) + 1

# import math


# def pageCount(n, p):
    
#     # Calcula o número total de páginas arredondando para cima
#     numero_de_paginas = math.ceil((n + 1) / 2)
    
#     # Calcula a página inicial que o leitor precisa virar para chegar à página desejada
#     primeira_pagina = p // 2
    
#     # Calcula a página final que o leitor precisa virar para chegar à página desejada
#     ultima_pagina = numero_de_paginas - primeira_pagina - 1
    
#     # Retorna a quantidade mínima de páginas que o leitor precisa virar
#     # para chegar à página desejada, levando em conta a contagem a partir do início
#     # e do final do livro
#     return min(primeira_pagina, ultima_pagina)


def pageCount(n, p):
    
    return min(p // 2, n // 2 - p // 2)


if __name__ == "__main__":
    
    n = int(input().strip())

    p = int(input().strip())

    resultado = pageCount(n, p)

    print(str(resultado) + '\n')