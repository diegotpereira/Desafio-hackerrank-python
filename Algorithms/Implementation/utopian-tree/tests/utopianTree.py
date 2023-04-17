# A Árvore Utópica passa por 2 ciclos de crescimento a cada ano. A cada primavera, 
# ela dobra de altura. A cada verão, sua altura aumenta em 1 metro.

# Uma muda de árvore utópica com 1 metro de altura é plantada no início da primavera. 
# Qual será a altura da árvore depoisciclos de crescimento?


# def utopianTree(n):
    
#     # começa com altura 1
#     altura = 1
    
#     # itera n vezes
#     for i in range(n):
        
#         # se for ímpar, adiciona 1 à altura
#         if i % 2 == 1:
            
#             # se for par, dobra a altura
#             # a altura da árvore é aumentada em 1 metro a cada verão
#             altura += 1
#         else:
#             altura *= 2
            
#     # retorna a altura final do ciclo n
#     return altura


# def utopianTree(n):
    
#      # Se n é igual a 0, a árvore não cresce
#     if n == 0:
        
#         altura = 1
        
#     else: 
        
#         # Altura inicial da árvore é 1
#         altura = 1
        
#         # Define o período de crescimento da árvore
#         periodo = range(1, n + 1)
        
#         for i in periodo:
            
#             if i % 2 != 0:
                
#                 # A cada verão, sua altura dobra
#                 altura *= 2
                
#             else:
                
#                 # cada primavera, sua altura aumenta em 1 metro
#                 altura += 1
                
#     return altura


# def utopianTree(n):
    
#     # Inicializa a altura como 1
#     altura = 1
#     # Contador para controlar o número de ciclos
#     contar = 0
    
#     # Executa o loop enquanto n é maior que zero
#     while n > 0:
        
#         # Se o contador é par, dobra a altura
#         if contar % 2 == 0:
            
#             altura *= 2
#             # Decrementa n e incrementa o contador
#             n -= 1
#             contar += 1
            
#         # Se o contador é ímpar, adiciona 1 à altura
#         else:
            
#             altura += 1
#             # Decrementa n e incrementa o contador
#             n -= 1
            
#             contar += 1
            
#     return altura

def utopianTree(n):
    
    # Se n é par, a fórmula 2**(n // 2 + 1) - 1 é usada para calcular a altura da árvore
    # Se n é ímpar, a função é chamada recursivamente com n + 1 e subtrai 1 do resultado final
    return 2**(n // 2 + 1) - 1 if n % 2 == 0 else utopianTree(n + 1) - 1

if __name__ == "__main__":
    
    t = int(input().strip())

    for t_itr in range(t):
        
        n = int(input().strip())

        resultado = utopianTree(n)

        print(str(resultado) + '\n')