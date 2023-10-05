# Você é um professor com n alunos 
# em sua turma. Você deseja dar a 
# cada aluno uma certa quantidade 
# de doces. Cada aluno deve receber 
# pelo menos um doce. Os alunos 
# têm classificações e você deseja 
# dar mais doces para os alunos que 
# têm classificações mais altas do 
# que seus vizinhos imediatos.

# No entanto, você deseja minimizar 
# a quantidade total de doces que 
# você dará. Como você faria isso?

# Escreva uma função que receba uma 
# lista de classificações dos alunos 
# e retorne o número mínimo de doces 
# que você precisa dar a eles para 
# satisfazer as condições dadas.

# def candies(n, arr):
    
#     # Inicializa uma lista de doces com todos os elementos iguais a 1
#     c = [1] * n 
    
#     # Percorre a lista da segunda posição até a última
#     for i in range(1, n):
        
#         # Verifica se a classificação do aluno atual 
#         # é maior que a do aluno anterior
#         if arr[i] > arr[i - 1]:
            
#             # Atribui um número de doces maior 
#             # ao aluno atual em relação ao anterior
#             c[i] = c[i - 1] + 1 
            
#     # Percorre a lista da penúltima posição até a primeira, 
#     # de forma reversa
#     for i in range(n - 2, - 1, - 1):
        
#         # Verifica se a classificação do aluno atual é maior que a do aluno seguinte e
#         # o número de doces atribuídos ao aluno atual não é maior do que o do aluno seguinte
#         if arr[i] > arr[i + 1] and c[i] <= c[i + 1]:
            
#             c[i] = c[i + 1] + 1
    
#     return sum(c)

# def candies(n, arr):
    
#     # Inicializa uma lista chamada "resultados" com todos os elementos iguais a 1
#     resultados = [1 for _ in range(n)]
    
#     # Percorre a lista da segunda posição até a última
#     for i in range(1, n):
        
#         # Verifica se a classificação do aluno atual é maior que a do aluno anterior
#         if arr[i] > arr[i - 1]:
            
#             # Atribui um número de doces maior ao aluno atual em relação ao anterior
#             resultados[i] = resultados[i - 1] + 1
            
#     # Percorre a lista da penúltima posição até a primeira, de forma reversa
#     for i in range(n - 2, - 1, -1):
        
#         # Verifica se a classificação do aluno atual é maior que a do aluno seguinte
#         if arr[i] > arr[i + 1]:
            
#             # Atribui o valor máximo entre o número de doces do aluno seguinte + 1 e o valor atual do aluno
#             resultados[i] = max(resultados[i + 1] + 1, resultados[i])
            
#     # Retorna a soma total dos números de doces atribuídos a todos os alunos
#     return sum(resultados)


def candies(n, arr):
    
    # Cria uma lista chamada "arr1" preenchida com 1, 
    # para armazenar as contagens crescentes
    arr1 = [1] * len(arr)
    
    # Cria uma lista chamada "arr2" preenchida com 1, 
    # para armazenar as contagens decrescentes
    arr2 = [1] * len(arr)
    
    # Percorre a lista da segunda posição até a última
    for n in range(1, len(arr)):
        
        # Atualiza arr1[n] para arr1[n-1] + 1 se a classificação 
        # atual for maior do que a anterior, caso contrário, atribui 1
        arr1[n] = arr1[n - 1] + 1 if arr[n] > arr[n - 1] else 1
        
    # Percorre a lista da penúltima posição até a primeira, 
    # de forma reversa
    for n in range(len(arr) - 2, -1, -1):
        
        # Atualiza arr2[n] para arr2[n+1] + 1 se a classificação 
        # atual for maior do que a seguinte, caso contrário, atribui 1
        arr2[n] = arr2[n + 1] + 1 if arr[n] > arr[n + 1] else 1
        
    # Calcula a soma das contagens máximas de ambas as listas arr1 e arr2 para cada posição n
    # Essa soma representa o mínimo total de doces distribuídos
    return sum(max(arr1[n], arr2[n]) for n in range(len(arr)))