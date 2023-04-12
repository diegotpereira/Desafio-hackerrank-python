# def migratoryBirds(arr):
    
#     # Inicializa a variável 'contar' como -1 e a variável 'id' como 0
#     contar = -1
#     id = 0
    
#     # Loop de 1 a 5, para cada tipo de pássaro
#     for i in range(1, 6):
        
#         # Conta o número de ocorrências do tipo de pássaro atual
#         # Se o número de ocorrências for maior do que a contagem atual, atualiza a contagem e o ID do pássaro mais comum
#         if (arr.count(i) > contar):
            
#             contar = arr.count(i)
#             id = i
            
#         # Se houver empate na contagem e o ID do pássaro atual for menor do que o ID do pássaro mais comum, atualiza o ID do pássaro mais comum
#         elif (arr.count(i) == contar and i < id):
            
#             id = i
            
#     # Retorna o ID do pássaro mais comum
#     return id


# def migratoryBirds(arr):
    
#     # Criando um conjunto (set) para armazenar valores únicos do array.
#     s = set(arr)
    
#     # Inicializando uma variável de contagem para a quantidade de ocorrências do pássaro mais comum.
#     contar = 0
    
#     # Inicializando uma lista vazia para armazenar os pássaros mais comuns.
#     res = []
    
#     # Looping pelos valores únicos do array.
#     for i in s:
        
#         # Verificando se a quantidade de ocorrências do pássaro atual é maior que a quantidade de ocorrências do pássaro mais comum até agora.
#         if arr.count(i) > contar:
            
#             # Se sim, atualizando a quantidade de ocorrências do pássaro mais comum.
#             contar = arr.count(i)
            
#     # Looping pelos valores únicos do array novamente.
#     for i in s:
        
#         # Verificando se a quantidade de ocorrências do pássaro atual é igual à quantidade de ocorrências do pássaro mais comum.
#         if arr.count(i) == contar:
            
#             # Se sim, adicionando o pássaro à lista de pássaros mais comuns.
#             res.append(i)
    
#     # Ordenando a lista de pássaros mais comuns em ordem crescente.
#     res.sort
    
#     # Retornando o primeiro pássaro da lista de pássaros mais comuns (que será o de menor ID).
#     return res[0]


def migratoryBirds(arr):
    
    # Iniciando a variável de contagem em zero.
    contar = 0
    
    # Ordenando o array em ordem crescente.
    arr.sort()
    
    # Looping pelos valores únicos do array.
    for i in set(arr):
        
        # Verificando se a quantidade de ocorrências do pássaro atual é maior do que a quantidade de ocorrências do pássaro mais comum até agora.
        if contar < arr.count(i):
            
            # Se sim, atualizando a quantidade de ocorrências do pássaro mais comum e o resultado atual.
            contar = arr.count(i)
            
            resultado = i 
            
    # Retornando o resultado (o ID do pássaro mais comum).
    return resultado


if __name__ == "__main__":
    
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')