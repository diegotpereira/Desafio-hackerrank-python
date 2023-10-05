# A tarefa do problema "Extra Long Factorials" 
# no HackerRank é calcular o fatorial de um número 
# grande e imprimir o resultado. A tarefa é desenvolvida 
# em linguagem de programação.

# O fatorial de um número inteiro não negativo 
# n (indicado por n!) é o produto de todos os 
# números inteiros positivos de 1 a n. Formalmente, 
# n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1.

# No entanto, o desafio nesse problema é que os 
# números para os quais o fatorial precisa ser 
# calculado são muito grandes para serem 
# representados usando tipos de dados inteiros 
# comuns. Portanto, a tarefa é implementar um 
# programa que possa lidar com cálculos de 
# fatorial para números grandes.

# def extraLongFactorials(n):
    
#     # Inicializa o resultado como 1, 
#     # pois qualquer número multiplicado por 1 é igual a ele mesmo
#     resultado = 1
    
#     # Loop que itera de n até 1 (descendo), 
#     # calculando o fatorial
#     for i in range(n, 0, -1):
        
#         # Multiplica o resultado atual pelo valor do iterador
#         resultado *= i 
    
#     # Retorna o resultado do cálculo do fatorial
#     return resultado

# def extraLongFactorials(n):
    
#     fato = 1
    
#     for i in range(2, n + 1):
        
#         fato *= i 
        
#     return fato

# def extraLongFactorials(n):
    
#     # Verifica se n é igual a 1
#     if n == 1:
        
#         # Retorna 1, pois o fatorial de 1 é 1
#         return 1
    
#     else:
        
#         # Caso n não seja 1, calcula n * fatorial de n - 1 usando recursão
#         return n * extraLongFactorials(n - 1)


def extraLongFactorials(n):
    
    resposta = 1
    
    for num in range(n, 0, -1):
        
        resposta *= num 
        
    return resposta