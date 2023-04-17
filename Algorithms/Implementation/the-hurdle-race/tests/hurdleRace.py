# Ler a altura máxima que o personagem consegue pular inicialmente e a lista de alturas dos obstáculos da corrida.

# Encontrar a altura do obstáculo mais alto da corrida.

# Verificar se a altura máxima inicial do personagem é maior ou igual à altura do obstáculo mais alto. Se sim, retornar 0, pois o personagem já consegue pular todos os obstáculos sem tomar a poção.

# Caso contrário, calcular a diferença entre a altura máxima inicial do personagem e a altura do obstáculo mais alto.

# Dividir a diferença encontrada no passo anterior por 1 (a quantidade de unidades que a poção aumenta a altura máxima do personagem por dose), e arredondar o resultado para cima com a função "math.ceil()".

# Retornar o resultado encontrado no passo anterior como o número de doses que o personagem precisa tomar para pular todos os obstáculos da corrida.

# k  representa a altura máxima de salto inicial do personagem.
# height lista que contém as alturas de cada obstáculo na corrida. 

def hurdleRace(k, height):
    
    # Encontra a altura máxima das barreiras
    altura_maxima = max(height)
    
    # Verifica se a altura máxima das barreiras é maior que a altura máxima que o personagem já pode saltar
    if altura_maxima > k:
        
        # retorna a diferença entre a altura máxima dos obstáculos e a 
        # altura máxima que o personagem pode pular sem usar a poção mágica
        return altura_maxima - k 
    
    return 0

# def hurdleRace(k, height):
    
#     f = max(height) - k
    
#     return f if f >= 0 else 0

# def hurdleRace(k, height):
    
#     # Calcula a diferença entre a altura máxima da barreira e a altura máxima do personagem
#     resultado = int(max(height) - k)
    
#     # Verifica se a diferença é maior que zero
#     if resultado > 0:
        
#         # Se a diferença for maior que zero, o personagem não consegue passar por todas as barreiras sem o uso da poção
#         # Retorna a quantidade de poções necessárias para o personagem passar por todas as barreiras
#         return resultado
    
#     else: 
        
#         # Se a diferença for menor ou igual a zero, o personagem consegue passar por todas as barreiras sem o uso da poção
#         # Retorna 0, indicando que nenhuma poção é necessária
#         return 0
    
    
    
if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()

    n = int(primeira_multipla_entrada[0])

    k = int(primeira_multipla_entrada[1])

    height = list(map(int, input().rstrip().split()))

    resultado = hurdleRace(k, height)

    print(str(resultado) + '\n')