

# def plusMinus(arr):
#     n = len(arr)
#     positive = sum(x > 0 for x in arr)
#     negative = sum(x < 0 for x in arr)
#     zero = sum(x == 0 for x in arr)
    
#     return (f"{round(positive / len(arr), 6)}\n{round(negative / len(arr), 6)}\n{round(zero / len(arr), 6)}")

# def plusMinus(arr):
    
#     # Inicializando as variáveis pos, neg e zeros com 0
#     pos, neg, zeros = 0, 0, 0
    
#     # Looping pelos elementos de arr
#     for n in arr:
        
#         # Verificando se o elemento é igual a zero
#         if n == 0:
            
#             # Incrementando a variável zeros
#             zeros += 1
        
#         # Verificando se o elemento é menor que zero
#         if n < 0:
            
#             # Incrementando a variável neg
#             neg += 1
            
#         # Verificando se o elemento é maior que zero
#         if n > 0:
            
#             # Incrementando a variável pos
#             pos += 1
            
#     # Retornando os resultados em formato de string com 6 casas decimais
#     return (f"{round(pos / len(arr), 6)}\n{round(neg / len(arr), 6)}\n{round(zeros / len(arr), 6)}")


if __name__ == '__main__':
    
    # Recebendo o valor de n como input e convertendo para inteiro
    n = int(input().strip())
    
    # Recebendo a lista de valores como input e convertendo para uma lista de inteiros
    arr = list(map(int, input().rstrip().split()))
    
    # Chamando a função plusMinus com a lista arr como parâmetro e armazenando o resultado na variável resultado
    resultado = plusMinus(arr)
    
    # Imprimindo o resultado na tela
    print(resultado)