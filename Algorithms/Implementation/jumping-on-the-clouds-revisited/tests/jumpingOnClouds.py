# Este problema envolve a simulação de um jogo em que um personagem deve saltar 
# entre nuvens em uma determinada sequência até chegar de volta à nuvem de partida, 
# com um certo nível de energia que é reduzido a cada salto e ainda diminui uma 
# quantidade adicional se o personagem pousar em uma nuvem de tempestade.

# A entrada para o problema inclui o número de nuvens, a distância de salto permitida 
# e uma matriz representando o tipo de nuvem em cada posição. O objetivo é determinar 
# o nível final de energia após o jogo terminar.

# Para resolver este problema, podemos criar um loop que simule cada salto do personagem. 
# A cada salto, verificamos se a próxima nuvem é uma nuvem de tempestade ou uma nuvem cumulus, 

# Para garantir que o caminho seja circular, devemos usar a operação de módulo para obter o 
# índice da próxima nuvem em relação ao tamanho do array. Isso é feito usando a expressão (i + k) % n, 
# onde i é o índice atual, k é a distância de salto e n é o número total de nuvens.


# Ler o número de nuvens e a distância de salto.
# Ler a matriz que representa as nuvens.
# Definir a energia inicial para 100.
# Definir a variável de índice para 0 (representando a primeira nuvem).
# Iniciar um loop enquanto o índice não chegar novamente à primeira nuvem.
# Dentro do loop, atualizar o índice para a próxima nuvem que o personagem deve saltar, usando a distância de salto e fazendo a operação módulo para garantir que a rota seja circular.
# Verificar se a nuvem atual é cumulus ou thunderhead e ajustar a energia de acordo: decrementar em 1 para nuvens cumulus e decrementar em 3 para nuvens thunderhead.
# Verificar se o índice atual é igual a 0. Se sim, sair do loop.
# Retornar a energia restante.
# Essa lógica é implementada nas duas soluções de código fornecidas anteriormente.

# def jumpingOnClouds(matriz_nuvens, distancia_salto):
    
#     # Obter o número total de nuvens
#     numero_total_nuvens = len(matriz_nuvens)
    
#     # Inicializar o nível de energia com 100
#     energia = 100
    
#     # Inicializar o índice atual como 0
#     i = 0
    
#     # Loop principal para simular os saltos do personagem
#     while True:
        
#         # Obter o índice da próxima nuvem usando a expressão (i + distancia_salto) % numero_total_nuvens
#         i = (i + distancia_salto) % numero_total_nuvens
        
#         # Reduzir o nível de energia em 1 unidade
#         energia -= 1  
        
#         # Se a próxima nuvem for uma nuvem de tempestade, reduzir o nível de energia em mais 2 unidades
#         if matriz_nuvens[i] == 1:
            
#             energia -= 2
            
#         # Verificar se o personagem voltou para a nuvem de partida
#         if i == 0:
            
#             # Se sim, interromper o loop
#             break
    
    
    
#     # Retornar o nível final de energia
#     return energia

# def jumpingOnClouds(matriz_nuvens, distancia_salto):
    
#     # Obtém o número de nuvens na matriz
#     numero_nuvens = len(matriz_nuvens)
    
#     # Inicializa o índice com a primeira nuvem que o 
#     # personagem irá saltar, usando o operador de módulo 
#     # para garantir que o índice esteja dentro dos limites da matriz
#     indice = (0 + distancia_salto) % numero_nuvens
    
#     # Define o nível inicial de energia do personagem, subtraindo 2 unidades 
#     # de energia para cada nuvem de trovão saltada e 1 unidade de energia para cada salto
#     energia = 99 - (matriz_nuvens[indice] * 2)
    
#     # Loop while para o personagem saltar de nuvem em nuvem até voltar para a nuvem de partida
#     while indice != 0:
        
#         # Calcula o índice da próxima nuvem que o personagem irá saltar
#         indice = (indice + distancia_salto) % numero_nuvens
        
#         # Atualiza o nível de energia do personagem, subtraindo 2 unidades de energia 
#         # para cada nuvem de trovão saltada e 1 unidade de energia para cada salto
#         energia =  energia - 1 - (matriz_nuvens[indice] * 2)
        
#     # Retorna o nível final de energia do personagem
#     return energia

def jumpingOnClouds(matriz_nuvens, distancia_salto):
    
    # Inicializa o índice com o número de nuvens que o personagem deve pular em cada salto
    pular = distancia_salto
    
    # Define o nível inicial de energia do personagem
    energia = 100
    
    # Loop while para o personagem saltar de nuvem em nuvem até voltar para a nuvem de partida
    while True:
        
        try:
            
            # Verifica se a nuvem atual é cumulus (0) ou thunderhead (1) e atualiza o nível de energia de acordo
            if matriz_nuvens[pular] == 0:
                
                energia -= 1
                
            elif matriz_nuvens[pular] == 1:
                
                energia -= 3
                
            # Verifica se o personagem voltou para a nuvem de partida e interrompe o loop se sim                
            if pular == 0:  
                
                break
            
            # Atualiza o índice para a próxima nuvem que o personagem irá saltar
            pular += distancia_salto
            
        except IndexError:
            
            # Se o personagem saltar além do final da matriz, ajusta o índice para a próxima nuvem usando o operador de módulo
            pular = (pular - len(matriz_nuvens))
            
        
    # Retorna o nível final de energia do personagem
    return energia

 
if __name__ == "__main__":
    
    nk = input().split()
    
    n = int(nk[0])
    
    k = int(nk[1])
    
    c = list(map(int, input().rstrip().split()))
    
    resultado = jumpingOnClouds(c, k)
    
    print(str(resultado) + '\n')