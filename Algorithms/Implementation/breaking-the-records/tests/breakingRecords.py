#  """
#     Essa função recebe como parâmetro uma lista de pontuações de um time em partidas e retorna um par de inteiros, 
#     onde o primeiro número representa a quantidade de vezes que o recorde de pontuação máxima foi quebrado e o 
#     segundo número representa a quantidade de vezes que o recorde de pontuação mínima foi quebrado.
# """


# def breakingRecords(pontuacoes):
    
#     # Inicializa as variáveis minimo e maximo com valor 0
#     minimo=0
#     maximo=0
    
#     # Percorre a lista de pontuações a partir do índice 1 até o último índice
#     for i in range(1,len(pontuacoes)):
        
#         # Verifica se a pontuação atual é menor do que a menor pontuação registrada até então
#         if  pontuacoes[i] < min(pontuacoes[0:i]):
            
#             # Se for menor, incrementa a variável minimo
#             minimo +=1
            
#         # Verifica se a pontuação atual é maior do que a maior pontuação registrada até então
#         elif pontuacoes[i] > max(pontuacoes[0:i]):
            
#             # Se for maior, incrementa a variável maximo
#             maximo += 1
    
#     # Retorna uma tupla com os valores de maximo e minimo
#     return maximo,minimo


# def breakingRecords(pontuacoes):
    
#     # contador para o número de vezes que o recorde foi quebrado
#     quebra_pontuacao = 0
#     # lista para armazenar o resultado
#     saida = []
    
#      # inicializa a variável do maior número com a primeira pontuação
#     maior_numero = pontuacoes[0]
    
#     # loop pelas pontuações para encontrar o número de vezes que o recorde de maior pontuação foi quebrado
#     for i in pontuacoes:
        
#         if (i > maior_numero):
            
#             quebra_pontuacao += 1
            
#             # atualiza a maior pontuação
#             maior_numero = i
            
#     # adiciona o número de vezes que o recorde de maior pontuação foi quebrado à lista de saída        
#     saida.append(quebra_pontuacao)
    
#     # reseta o contador para o número de vezes que o recorde foi quebrado
#     quebra_pontuacao = 0
#     # inicializa a variável do menor número com a primeira pontuação
#     menor_numero = pontuacoes[0]
    
#     # loop pelas pontuações para encontrar o número de vezes que o recorde de menor pontuação foi quebrado
#     for p in pontuacoes:
        
#         if(p < menor_numero):
            
#             quebra_pontuacao += 1
#             # atualiza a menor pontuação
#             menor_numero = p
            
#     # adiciona o número de vezes que o recorde de menor pontuação foi quebrado à lista de saída
#     saida.append(quebra_pontuacao)
    
#     # retorna a tupla de saída contendo o número de vezes que o recorde de maior e menor pontuação foi quebrado, respectivamente
#     return tuple(saida)

def breakingRecords(scores):
    
    # inicializa as variáveis que contam as quebras de recordes
    minimo=0
    maximo=0
    
    # itera sobre todas as pontuações
    for i in range(1,len(scores)):
        
        # verifica se a pontuação atual é menor que a menor pontuação anterior
        if  scores[i] < min(scores[0:i]):
            minimo +=1
            
        # verifica se a pontuação atual é maior que a maior pontuação anterior
        elif scores[i] > max(scores[0:i]):
            maximo += 1
    
    # retorna uma tupla com a quantidade de quebras de recorde de maior e menor pontuação
    return maximo,minimo

if __name__ == "__main__":
    
    n = int(input().strip())
    
    pontuacoes = list(map(int, input().rstrip().split()))
    
    resultado = breakingRecords(pontuacoes)
    
    print(' '.join(map(str, resultado)))
    print('\n')