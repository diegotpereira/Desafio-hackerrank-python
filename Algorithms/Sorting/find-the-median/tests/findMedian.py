# Dada uma matriz de números inteiros, você deve 
# encontrar a mediana da matriz. A mediana é o 
# valor que divide a matriz em duas metades iguais: 
# uma metade contendo todos os números menores ou 
# iguais à mediana, e a outra metade contendo todos 
# os números maiores ou iguais à mediana.

# def findMedian(arr):
    
#     # Ordena a matriz em ordem crescente
#     arr = sorted(arr)
    
#     # Retorna o valor mediano da matriz.
#     # Se a matriz tiver um número ímpar de elementos, o valor mediano é o elemento central.
#     # Se a matriz tiver um número par de elementos, o valor mediano é a média dos dois elementos centrais.
#     return arr[len(arr) // 2]


# def findMedian(arr):
    
#      # Obtém o tamanho da matriz
#     tamanho = len(arr)
    
#     # Cria uma lista chamada "valor" com 20001 
#     # elementos, todos inicializados como 0.
#     valor = [0] * 20001
    
#     # Variável para armazenar a soma dos valores 
#     # de "valor" ao percorrer a matriz "arr"
#     soma = 0
    
#     # Percorre a matriz "arr" e incrementa o contador 
#     # de "valor" para cada elemento encontrado.
#     # Note que é utilizado o deslocamento "entrada + 10000" 
#     # para acomodar valores negativos, se houver.
#     for entrada in arr:
        
#         valor[entrada + 10000] += 1
        
#     # Percorre a lista "valor".
#     for i in range(len(valor)):
        
#         # Soma o valor atual de "valor[i]" na variável "soma"
#         soma += valor[i]
        
#         # Verifica se a "soma" é maior que a metade do tamanho da matriz "arr".
#         # Se for, o valor atual de "i - 10000" representa a mediana.
#         # (Lembrando que o valor de "i" representa a posição na matriz original, 
#         # então subtraímos 10000 para obter o valor real.)
#         if soma > tamanho // 2:
            
#             return i - 10000


# def findMedian(arr):
    
#     # Inicializa um array chamado "array_inicial" com 10000 elementos, 
#     # todos inicializados como 0.
#     array_inicial = []
#     array_classificado = []
    
#     for i in range(0, 10000):
        
#         array_inicial.append(0)
        
#     # Conta a ocorrência de cada valor presente na matriz "arr" e armazena 
#     # em "array_inicial".
#     # Cada índice do array representa um valor possível em "arr" e seu valor 
#     # é a quantidade de ocorrências.
#     for i in arr:
        
#         array_inicial[i] += 1
        
#     # Cria um novo array chamado "array_classificado" com todos os valores 
#     # presentes em "arr",
#     # onde cada valor é repetido de acordo com a sua ocorrência em 
#     # "array_inicial".
#     for indice, i in enumerate(array_inicial):
        
#         for valor in range(i):
            
#             array_classificado.append(indice)
            
#     # Calcula a mediana do "array_classificado" e retorna o valor correspondente.
#     # Se o tamanho do array for ímpar, a mediana é o elemento central.
#     # Se o tamanho do array for par, a mediana é a média dos dois elementos centrais.
#     return array_classificado[((len(array_classificado) + 1) // 2) - 1]


def findMedian(arr):
    
    # Ordena a matriz "arr" em ordem crescente.
    arr.sort()
    
    # Calcula o índice do elemento mediano na 
    # matriz ordenada "arr".
    # O operador "//" realiza uma divisão inteira, 
    # resultando em um valor arredondado para baixo, 
    # caso o tamanho da matriz seja ímpar.
    a = len(arr) // 2
    
    # Retorna o elemento mediano da matriz "arr", 
    # que está na posição "a".
    # Se o tamanho da matriz for ímpar, "a" apontará 
    # diretamente para o elemento mediano.
    # Se o tamanho da matriz for par, "a" apontará para 
    # o primeiro elemento do par mediano.
    return arr[a]