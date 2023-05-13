# def squares(a, b):
    
#     # Inicialização da variável de resultado
#     res = 0
    
#     # Inicialização do contador
#     i = 1
    
#     # Loop infinito
#     while True:
        
#         # Verifica se o quadrado de i está entre a e b (inclusive)
#         if (i * i >=  a and i * i <= b):
            
#             # Incrementa o resultado
#             res += 1
            
#         # Verifica se o quadrado de i é maior que b
#         if (i * i > b):
            
#             # Sai do loop
#             break
        
#         else:
            
#             # Incrementa o contador
#             i += 1
            
#     # Retorna o resultado
#     return res

# import math


# def squares(a, b):
    
#     # Variável para contar a 
#     # quantidade de números quadrados entre 'a' e 'b'
#     contar = 0
    
#     # Calcula a raiz quadrada de 'a' e converte para inteiro
#     raiz_a = int(math.sqrt(a))
    
#     # Calcula a raiz quadrada de 'b' e converte para inteiro
#     raiz_b = int(math.sqrt(b))
    
#      # Verifica se 'a' é um número quadrado perfeito
#     if (raiz_a * raiz_a) == a:
        
#         # Incrementa o contador se 'a' for um número quadrado perfeito
#         contar += 1
        
#     # Retorna a diferença entre as raízes e adiciona o contador
#     return (raiz_b - raiz_a) + contar


# import math


# def squares(a, b):
    
#     # Calcula a raiz quadrada de 'a' e arredonda para cima
#     a = math.ceil(a ** 0.5)
    
#     # Calcula a raiz quadrada de 'b' e arredonda para baixo
#     b = math.floor(b ** 0.5)
    
#     # Retorna a diferença entre 'b' e 'a', 
#     # adiciona 1 para incluir o limite superior 'b'
#     return b - a + 1

