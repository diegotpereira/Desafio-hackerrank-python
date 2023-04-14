

# def pickingNumbers(a):
    
#     # Inicializa uma lista com 100 elementos iguais a zero
#     contar = [0] * 100
    
#     # Conta a frequência de cada elemento no array 'a'
#     for i in a:
        
#         contar[i] += 1
        
#     # Inicializa uma variável para armazenar o tamanho máximo encontrado
#     tamanho_maximo = 0
    
#     # Itera pelos elementos de 1 a 99
#     for i in range(1, 100):
        
#         # tamanho_maximo = max(tamanho_maximo, contar[i] + contar[i - 1])
        
#         # Calcula o tamanho do subarray onde a diferença absoluta
#         # entre quaisquer dois elementos é menor ou igual a 1
#         tamanho_atual = contar[i] + contar[i - 1]
        
#         # Atualiza a variável 'tamanho_maximo' se o tamanho atual
#         # é maior que o tamanho máximo encontrado até agora
#         tamanho_maximo = max(tamanho_maximo, tamanho_atual)
        
#     # Retorna o tamanho máximo encontrado
#     return tamanho_maximo
    
    
# def pickingNumbers(a):
    
#     # Transforma a lista em um conjunto e depois novamente em uma lista 
#     # Transformar a lista em um conjunto é uma maneira conveniente de remover 
#     # duplicatas da lista, já que os conjuntos só podem ter elementos únicos.
#     s =list(set(a))
    
#     # Inicializa a variável maximo com 0
#     maximo = 0
    
#     # Percorre cada elemento do conjunto s
#     for i in s:
        
#         # Conta a quantidade de ocorrências do elemento i e do seu elemento anterior (i-1) na lista a
#         c = a.count(i) + a.count(i - 1)
        
        
#         # Se o valor de c for maior que o valor de maximo, atualiza maximo com o valor de c
#         if (maximo < c):
            
#             maximo = c
            
    # Retorna o valor máximo encontrado
    # return maximo
    
def pickingNumbers(a):
    
    # variável que armazena a maior quantidade de números
    maior = 0
    
    # cria uma lista de 100 elementos com valor 0
    dic = [0 for i in range(100)]
    
    # percorre a lista 'a'
    for s in a:
        
        # incrementa o valor da posição 's' na lista 'dic'
        dic[s] += 1
        
    # percorre a lista 'dic' até o índice 99
    for i in range(99):
        
        # soma os valores das posições 'i' e 'i+1' na lista 'dic'
        agora = sum((dic[i], dic[i + 1]))
        
        # verifica se a soma é maior que a maior quantidade de números atual
        if agora > maior:
            
            # atualiza a maior quantidade de números
            maior = agora
            
    # retorna a maior quantidade de números possíveis.
    return maior

if __name__ == "__main__":
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    resultado = pickingNumbers(a)

    print(str(resultado) + '\n')