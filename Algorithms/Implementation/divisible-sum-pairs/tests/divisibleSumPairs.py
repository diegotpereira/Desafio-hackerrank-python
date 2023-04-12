# def divisibleSumPairs(n, k, ar):
    
#     # Inicializa a variável `contar` com zero.
#     contar = 0
    
#     # Percorre a lista `ar` de índice 0 até o índice `n - 1`.
#     for i in range(n):
        
#         # Percorre a lista `ar` a partir do índice `i + 1` até o índice `n - 1`.
#         for j in range(i + 1, n):
            
#             # Verifica se a soma dos elementos `ar[i]` e `ar[j]` é divisível por `k`.
#             # O resultado da expressão `(ar[i] + ar[j]) % k == 0` é um valor booleano (True ou False).
#             # Se for True, adiciona 1 ao valor de `contar`, pois encontramos um par de elementos que satisfazem a condição.
#             # Se for False, não faz nada.
#             contar += ((ar[i] + ar[j]) % k == 0)
            
#     # Retorna o valor final de `contar`.
#     return contar 

# def divisibleSumPairs(n, k, ar):
    
#     # inicializa um contador para contar quantos pares satisfazem a condição
#     conta = 0
    
#      # percorre o array do índice 0 até o penúltimo índice
#     for i in range(0, n - 1):
        
#         # inicializa a soma dos dois elementos com zero
#         add = 0
        
#         # percorre o array a partir do índice atual i até o último índice n-1
#         for j in range(i, n):
            
#             # calcula a soma dos dois elementos atuais
#             add = ar[i] + ar[j]
            
#             # verifica se a soma é divisível por k e se os índices não são iguais
#             if add % k == 0 and i != j:
                
#                 # incrementa o contador se a condição for satisfeita
#                 conta += 1
    
#     # retorna o número de pares encontrados que satisfazem a condição     
#     return conta

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()

    n = int(primeira_multipla_entrada[0])

    k = int(primeira_multipla_entrada[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')