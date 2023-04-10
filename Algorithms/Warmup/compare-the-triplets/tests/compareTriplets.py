# Esse código define uma função compareTriplets que recebe duas listas a e b. O objetivo da função é 
# comparar elementos correspondentes nas listas a e b e atribuir pontos aos jogadores correspondentes. 
# A função retorna uma lista com dois elementos, onde o primeiro elemento é a pontuação do jogador 1 e 
# o segundo elemento é a pontuação do jogador 2.

# O programa também recebe entrada do usuário, duas listas de números separados por espaço. Em seguida, 
# a função compareTriplets é chamada com as duas listas como argumentos. O resultado é armazenado em uma 
# variável resultado e é impresso na tela.

# A função compareTriplets recebe duas listas de inteiros a e b como parâmetro. Ela compara os elementos 
# correspondentes em ambas as listas (o primeiro elemento em a com o primeiro elemento em b, o segundo elemento
# em a com o segundo elemento em b, etc.) e determina qual dos elementos é maior. Se o elemento correspondente 
# a for maior que o elemento correspondente em b, então o primeiro elemento da lista pontos é incrementado em 1. 
# Se o elemento correspondente em b for maior que o elemento correspondente em a, então o segundo elemento da lista 
# pontos é incrementado em 1.

def compareTriplets(a, b):
    
    #
    # A segunda linha da função usa uma compreensão de lista para criar uma lista de tuplas (ae>be, be>ae) comparando os elementos correspondentes de a e b.
    # A função zip combina as duas listas a e b, agrupando os elementos correspondentes em tuplas, que são usadas na compreensão de lista.
    # A função map e sum são usadas para calcular a soma dos valores booleanos True (que representam vitórias) e False (que representam derrotas) em cada tupla da lista criada na compreensão de lista.
    # A função zip é usada novamente para combinar os resultados da soma das vitórias e das derrotas em uma única lista.

    return list(map(sum, zip(*[(ae > be, be > ae) for ae, be in zip(a, b)])))

# def compareTriplets(a, b):
    
#     pontos = [0] * 2
    
#     for i in range(len(a)):
        
#         if a[i] > b[i]:
            
#             pontos[0] += 1
            
#         if b[i] > a[i]:
            
#             pontos[1] += 1
    
#     return pontos

if __name__ == '__main__':
    
    # Recebe a entrada do usuário
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    # Chama a função compareTriplets
    resultado = compareTriplets(a, b)
    
    # imprime a saída na tela
    print(' '.join(map(str, resultado)))