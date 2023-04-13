# passos número de passos na caminhada
# caminho string descrevendo o caminho

# def countingValleys(passos, caminho):
    
#     # contador para contar o número de vales percorridos
#     contar = 0
    
#     # contador para rastrear a altitude do caminhante
#     altitude = 0
    
    
#     for i in range(0, passos):
        
#         # o caminhante deu um passo para cima
#         if caminho[i] == "U":
            
#             # incrementa a altitude
#             altitude += 1
            
#             # se voltou ao nível do mar após uma sequência abaixo do nível do mar
#             if altitude == 0:
                
#                 # incrementa o contador de vales
#                 contar += 1
        
#         # o caminhante deu um passo para baixo
#         else:
            
#             # decrementa a altitude
#             altitude -= 1
            
#     return contar


def countingValleys(passos, caminho):
    
     # criando uma lista para armazenar os vales
    vales = []
    
    # contadores para os passos para cima e para baixo
    passo_para_cima = 0
    passo_para_baixo = 0
    
    # iterando sobre cada elemento do caminho
    for i in caminho:
        
        # se o passo for para cima, incrementa o contador de passos para cima
        if i == 'U':
            
            passo_para_cima += 1
            
            # se o número de passos para baixo for igual ao número de passos para cima,
            # significa que estamos de volta ao nível do mar e, portanto, acabamos de sair de um vale
            if passo_para_baixo - passo_para_cima == 0:
                
                # adiciona 1 à lista de vales
                vales.append(1)
                
        # se o passo for para baixo, incrementa o contador de passos para baixo
        if i == 'D':
            
            passo_para_baixo += 1
            
    # retorna a soma dos elementos da lista de vales
    return sum(vales)


if __name__ == "__main__":
    
    passos = int(input().strip())

    caminho = input()

    result = countingValleys(passos, caminho)

    print(str(result) + '\n')