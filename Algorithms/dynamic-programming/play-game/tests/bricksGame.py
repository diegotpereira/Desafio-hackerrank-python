
# A tarefa do problema "Play Game" é determinar 
# o número máximo de pontos que um jogador pode 
# ganhar em um jogo com regras específicas. O 
# jogo envolve uma sequência de números, e o 
# jogador pode escolher entre três opções em cada etapa:

# Remover o último número da sequência.
# Remover os dois últimos números da sequência.
# Remover os três últimos números da sequência.
# O jogador ganha pontos igual ao número que 
# ele removeu. O objetivo é maximizar o número 
# total de pontos que o jogador ganha após a 
# remoção de todos os números. O jogador pode 
# escolher sabiamente para obter a pontuação máxima possível.

# A entrada do problema consiste em uma sequência 
# de números e você precisa calcular a pontuação 
# máxima que um jogador pode obter seguindo as regras acima.

# Você deve implementar uma função que receba a 
# sequência de números e retorne a pontuação máxima 
# que pode ser alcançada pelo jogador.

# def bricksGame(arr):
    
#     # Obtém o comprimento da lista de entrada
#     n = len(arr)
    
#     # Se a lista tiver menos de 4 elementos, 
#     if n < 4:
        
#         # retorna a soma de todos os elementos
#         return sum(arr)
    
#     # Inverte a lista de entrada para facilitar a iteração
#     rev = arr[::-1]
    
#     # Cria listas para armazenar pontuação e somas parciais
#     pontuacao = [0] * n 
#     somas = [0] * n 
    
#     # Inicializa os valores das primeiras três posições das listas
#     somas[0] = pontuacao[0] = rev[0]
#     somas[1] = pontuacao[1] = rev[0] + rev[1]
#     somas[2] = pontuacao[2] = rev[0] + rev[1] + rev[2]
    
#     # Calcula a pontuação máxima para cada posição
#     for i in range(3, n):
        
#         # Calcula as somas parciais
#         somas[i] = somas[i - 1] + rev[i]
        
#         # Calcula as possíveis pontuações para esta posição
#         b1 = rev[i] + somas[i - 1] - pontuacao[i - 1]
#         b2 = rev[i - 1] + rev[i] + somas[i - 2] - pontuacao[i - 2]
#         b3 = rev[i - 2] + rev[i - 1] + rev[i] + somas[i - 3] - pontuacao[i - 3]
        
#         # Atribui a pontuação máxima para esta posição
#         pontuacao[i] = max(b1, b2, b3)
        
#     # Retorna a pontuação máxima
#     return pontuacao[-1]

# def bricksGame(arr):
    
#     # Obtém o tamanho do array de entrada.
#     n = len(arr)
    
#     # Inicializa um array dp com zeros para 
#     # armazenar as pontuações máximas.
#     dp = [0] * (n + 3)
    
#     # Inicializa uma variável s para rastrear 
#     # a soma cumulativa dos elementos do array.
#     s = 0
    
#     # Loop reverso que calcula as pontuações 
#     # máximas a partir do final do array.
#     for i in range(n - 1, -1, -1):
        
#         # Adiciona o valor atual ao somatório cumulativo.
#         s += arr[i]
        
#         # Calcula a pontuação máxima para a posição i com base nas três jogadas possíveis.
#         # A pontuação máxima é a soma acumulativa subtraída da menor pontuação nas próximas três posições.
#         dp[i] = s-(min(dp[i + 1], dp[i + 2], dp[i + 3]))
        
#     # Retorna a pontuação máxima no início do jogo (posição 0).
#     return dp[0]


def bricksGame(arr):
    
    # Obtém o tamanho do array.
    lenArr = len(arr)
    
    # Cria uma lista `dp` para armazenar as pontuações máximas.
    dp = [0] * (lenArr + 1)
    
    # Inverte o array original, já que o cálculo começa a partir do final.
    tijolos = list(reversed(arr))
    
    # Cria uma lista `soma` para armazenar as somas acumulativas.
    soma = [0] * (lenArr + 1)
    
    for i in range(1, len(arr) + 1):
        
         # Calcula a soma acumulativa até a posição `i`.
        soma[i] = soma[i - 1] + tijolos[i - 1]
        
        # Se `i` for menor ou igual a 3, 
        if i <= 3:
            
            # a pontuação máxima é a soma total até `i`.
            dp[i] = sum(tijolos[:i])
            
        else:
            
            a = tijolos[i - 1] - dp[i - 1] + soma[i - 1]
            b = sum(tijolos[i - 2:i]) - dp[i - 2] + soma[i - 2]
            c = sum(tijolos[i - 3:i]) - dp[i - 3] + soma[i - 3]
            
            # Calcula a pontuação máxima para a posição `i` com base nas próximas posições.
            dp[i] = max(a, b, c)
            
    # Retorna a pontuação máxima para a posição final.
    return dp[lenArr]
    