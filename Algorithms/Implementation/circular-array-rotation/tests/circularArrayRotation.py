# def circularArrayRotation(arr, numero_rotacoes, consultas):
    
#     # print("fim")
    
#     # Cria uma lista vazia para armazenar os valores das consultas
#     valor = []
    
#     # Realiza a operação de rotação no array
#     arr_rotacao = arr[-numero_rotacoes:] + arr[:-numero_rotacoes]
    
#     # Itera sobre as consultas
#     for q in consultas:
        
#         # Adiciona o valor da consulta à lista de valores
#         valor.append(arr_rotacao[q])
    
#     # Retorna a lista de valores das consultas
#     return valor

# def circularArrayRotation(arr, numero_rotacoes, consultas):
    
#     # guarda o tamanho do array 
#     n = len(arr)
    
#     # utiliza a fórmula de indexação circular para acessar os elementos
#     # desejados após as rotações
#     return [arr[(i - numero_rotacoes + n) % n] for i in consultas]

# def circularArrayRotation(arr, numero_rotacoes, consultas):
    
#     # Realiza a operação módulo para evitar que o número de rotações seja maior que o tamanho do array
#     numero_rotacoes = numero_rotacoes % len(arr)
    
#     # Realiza a rotação do array de acordo com o número de rotações especificado
#     # A lista resultante contém os dois últimos elementos da lista original.
#     arr = arr[-numero_rotacoes:] + arr[:-numero_rotacoes]
    
#     # Inicializa a lista onde serão armazenados os resultados das consultas
#     resultado = []
    
#     # Percorre as posições especificadas nas consultas
#     for q in consultas:
        
#         # adiciona o valor correspondente na lista de resultados
#         resultado.append(arr[q])
        
#     # Retorna a lista com os resultados das consultas
#     return resultado

def circularArrayRotation(arr, numero_rotacoes, consultas):
    
    novo = []
    
    # realiza as rotações no array
    for i in range(numero_rotacoes):
        
        # retira o último elemento do array
        ultimo = arr.pop()
        
        # insere o último elemento na primeira posição do array
        arr.insert(0, ultimo)
        
        
    # consulta os elementos do array nas posições especificadas
    for q in consultas:
        
        # adiciona o valor do elemento na posição q do array à lista de resultados
        novo.append(arr[q])
        
    return novo


if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    numero_rotacoes = int(primeira_multipla_entrada[1])
    q = int(primeira_multipla_entrada[2])
    
    arr = list(map(int, input().rstrip().split()))
    
    consultas = []
    
    for i in range(q):
        
        itens_consulta = int(input().strip())
        consultas.append(itens_consulta)
        
    resultado = circularArrayRotation(arr, numero_rotacoes, consultas)
    
    # print(arr)
    # print(numero_rotacoes)
    # print(consultas)
    
    print('\n'.join(map(str, resultado)))
    print('\n')