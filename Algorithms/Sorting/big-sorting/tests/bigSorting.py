# No problema "big sorting" do HackerRank, 
# a tarefa é classificar um conjunto de 
# números inteiros grandes em ordem 
# não decrescente.

# Mais especificamente, você receberá 
# uma lista de números inteiros como 
# entrada, e sua tarefa é escrever um 
# programa para ordenar esses números 
# de forma que os números maiores 
# apareçam após os menores. No entanto, 
# a complexidade desse problema está no 
# fato de que os números podem ser muito
# grandes e não caber em tipos de dados 
# comuns, como inteiros ou ponto flutuante.

# Você deve implementar uma solução que 
# lide com números grandes e os ordene 
# corretamente. A ordem deve ser baseada 
# nos valores dos números, e não em suas 
# representações de string. Portanto, é 
# necessário implementar uma ordenação 
# personalizada para esse problema.

# Lembre-se de considerar a eficiência do 
# algoritmo, pois você pode ter que lidar
# com um grande número de elementos na 
# lista. Certifique-se de que sua solução 
# funcione dentro dos limites de tempo 
# estabelecidos pelo HackerRank.

# # Define a função bigSorting que recebe uma lista de números como entrada

# def bigSorting(n):
    
#     # Cria um dicionário vazio para armazenar 
#     # números com base no comprimento de suas representações
#     dic = {}
    
#     # Itera sobre a lista de números de entrada
#     for num in n:
        
#         # Calcula o comprimento da representação do número
#         chave = len(num)
        
#         # Verifica se o comprimento já existe como chave no dicionário
#         if chave in dic:
            
#             # Se existir, 
#             # adiciona o número à lista existente associada à chave
#             dic[chave].append(num)
            
#         else:
            
#             # Se não existir, 
#             # cria uma nova entrada no dicionário com a chave e uma lista contendo o número
#             dic[chave] = [num]
            
#     # Cria uma lista de listas ordenadas com base nas chaves (comprimentos) do dicionário
#     classificar_dic = [sorted(dic[i]) for i in sorted(dic.keys())]
    
#     # Retorna uma lista achatada, que é a lista ordenada final
#     return ([i for subLista in classificar_dic for i in subLista])


# # Define a função bigSorting que recebe uma lista de strings como entrada

# def bigSorting(n):
    
#     # Usa a função `sorted` para classificar a lista de strings
#     # A chave de classificação é uma função lambda que considera o comprimento da string e a própria string como critérios de ordenação
#     # Isso classificará a lista primeiro pelo comprimento das strings e, em seguida, lexicograficamente (ordem alfabética)
#     return sorted(n, key=lambda s: (len(s), s))

# Importa a classe defaultdict do módulo collections

from collections import defaultdict

# Define a função bigSorting que recebe uma lista de strings como entrada

def bigSorting(naoTriadas):
    
    # Cria um dicionário com valores padrão de lista para 
    # armazenar números com base no comprimento de suas representações
    numeros = defaultdict(list)
    
    # Itera sobre a lista de números de entrada
    for numero in naoTriadas:
        
        # Calcula o comprimento da representação do número
        tamanho = len(numero)
        
        # Adiciona o número à lista correspondente com base em seu comprimento no dicionário "numeros"
        numeros[tamanho].append(numero)
        
        # Inicializa uma lista "resultado" para armazenar o resultado final
        resultado = []
        
        # Itera sobre as chaves do dicionário "numeros" em ordem crescente
        for l in sorted(numeros.keys()):
            
            # Ordena os números na lista correspondente e adiciona-os à lista "resultado"
            resultado += sorted(numeros[l])
            
    # Retorna o resultado final, que é uma lista de números ordenados por comprimento e valor
    return resultado