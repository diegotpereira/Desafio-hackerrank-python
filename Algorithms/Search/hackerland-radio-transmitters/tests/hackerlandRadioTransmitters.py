# Dada uma série de casas localizadas em uma linha em 
# que cada casa está localizada em uma posição específica, 
# o objetivo é instalar transmissores de rádio em algumas 
# casas de forma que o alcance de cada transmissor seja 
# o mesmo. O alcance de um transmissor é uma variável inteira.

# A tarefa pode ser resumida nas seguintes etapas:

# Receba uma lista de posições das casas em uma linha,
# onde cada posição é representada por um número inteiro.
# Receba o alcance máximo de cada transmissor, que é 
# um número inteiro.
# Determine a quantidade mínima de transmissores 
# necessários para cobrir todas as casas de modo 
# que o alcance de cada transmissor seja o mesmo.
# Instale os transmissores nas posições das casas 
# de forma a minimizar a quantidade de transmissores.

# k = alcance de cada transmisso
# x = localização das casas

# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Ordenar a lista de posições das casas em ordem crescente
#     localizacao_casa.sort()
    
#     # Inicializar a variavel resultado como 0.
#     resultado = 0
    
#     # Inicializar a distância máxima como 0.
#     maxDist = 0
    
#     # Inicializar a distância do transmissor como alcance_transmissor.
#     distTrans = alcance_transmissor
    
#     for i in range(len(localizacao_casa) - 1):
        
#         # Se a casa atual já está coberta, continue para a próxima casa.
#         if localizacao_casa[i] <= maxDist:
            
#             continue
        
#         else:
            
#             # Se a próxima casa pode ser coberta pelo transmissor atual
#             if localizacao_casa[i + 1] <= localizacao_casa[i] + distTrans:
                
#                 # ajuste a distância do transmissor.
#                 distTrans = localizacao_casa[i] + distTrans - localizacao_casa[i + 1]
                
#             else:
                
#                 # Se a próxima casa não pode ser coberta pelo transmissor atual,
#                 # instale um novo transmissor na casa atual.
#                 resultado += 1
                
#                 # Redefinir a distância do transmissor para alcance_transmissor.
#                 distTrans = alcance_transmissor 
                
#                 # Atualizar a distância máxima.
#                 maxDist = localizacao_casa[i] + alcance_transmissor
                
#     # Se a última casa não está coberta
#     if localizacao_casa[-1] > maxDist:
        
#         # instale um transmissor nela.
#         resultado += 1
    
#     return resultado


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Classifique as localizações das casas em ordem crescente.
#     arr = sorted(localizacao_casa) 
    
#     # Obtém o número total de casas.
#     numero_total_casas = len(localizacao_casa)
    
#     # Inicializa a posição do transmissor na primeira casa
#     posicao_inicial_casa = arr[0]
    
#     # Define uma bandeira para controlar a busca do próximo transmissor.
#     buscar_casa = True
    
#     # Inicializa o contador de transmissores com 1, considerando o primeiro.
#     contador_transmissor = 1
    
#     for i in range(numero_total_casas):
        
#         if arr[i] - posicao_inicial_casa > alcance_transmissor:
            
#             # Se a distância entre a casa atual e o potencial transmissor for maior que o alcance do transmissor:
#             if arr[i] - arr[i - 1] <= alcance_transmissor and buscar_casa:
                
#                 # Se a casa anterior estiver no alcance do transmissor 
#                 # e a bandeira estiver definida, 
#                 # use a casa anterior como potencial.
#                 posicao_inicial_casa = arr[i - 1]
#                 buscar_casa = False
                
#             else:
                
#                 # Caso contrário, posicione um novo transmissor na casa atual.
#                 posicao_inicial_casa = arr[i]
                
#                  # Aumenta o contador de transmissores.
#                 contador_transmissor += 1
#                 buscar_casa = True
    
#     # Retorna o número mínimo de transmissores necessários.
#     return contador_transmissor


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Inicialize o contador de torres.
#     torres = 0
    
#     # Ordene as localizações das casas.
#     localizacao_casa.sort()
    
#     # Adicione uma posição fictícia para tratar o final da lista.
#     localizacao_casa.append(-1)
    
#     # Inicialize um índice para percorrer as localizações das casas.
#     i = 0
    
#     while i < len(localizacao_casa):
        
#         # Calcule a posição ideal para a torre.
#         localizacao_ideal = localizacao_casa[i] + alcance_transmissor
        
#         # Calcule o alcance da torre.
#         alcance_torre = range(localizacao_casa[i], localizacao_ideal + 1)
        
#         # Inicialize o índice da torre.
#         indice_torre = i 
        
#         while localizacao_casa[indice_torre + 1] in alcance_torre:
            
#             # Encontre o local onde a torre pode ser instalada com base no alcance.
#             if indice_torre == len(localizacao_casa) - 1:
                
#                 break 
            
#             indice_torre += 1
            
#         # Determine a posição da torre.
#         torre = localizacao_casa[indice_torre]
        
#         # Calcule o alcance máximo da torre.
#         alcance_maximo = torre + alcance_transmissor
        
#         while localizacao_casa[i] <= alcance_maximo:
            
#             # Avance para a próxima casa que pode ser coberta por esta torre.
#             i += 1
            
#             if i >= len(localizacao_casa):
                
#                 break
        
#         # Incremente o contador de torres.
#         torres += 1
        
#     # Retorna o número mínimo de torres necessárias.
#     return torres


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Ordene as localizações das casas.
#     localizacao_casa.sort()
    
#     # Inicialize o contador de transmissores.
#     trasmissores = 0
    
#     # Comece no último índice da lista de localizações.
#     indice = len(localizacao_casa) - 1
    
#     while indice >= 0:
        
#         for _ in range(2):
            
#             # Inicialize a distância restante do alcance do transmissor.
#             restante = alcance_transmissor
            
#             # Enquanto houver alcance e casas para percorrer.
#             while restante >= 0 and indice >= 1:
                
#                 atual, proximo = localizacao_casa[indice], localizacao_casa[indice - 1]
                
#                 # Calcule a diferença entre as localizações.
#                 diferenca = atual - proximo
                
#                 # Subtraia a diferença do alcance restante.
#                 restante -= diferenca
                
#                  # Se ainda houver alcance restante
#                 if restante >= 0:
                    
#                     # avance para a próxima casa.
#                     indice -= 1
                    
                    
#          # Incremente o contador de transmissores.
#         trasmissores += 1
        
#         # Avance para a próxima casa.
#         indice -= 1
            
#     # Retorna o número mínimo de transmissores necessários.
#     return trasmissores


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Ordene as localizações das casas.
#     localizacao_casa.sort()
    
#     # Inicialize a localização da primeira casa.
#     primeira_casa = localizacao_casa[0]
    
#     # Inicialize o número de antenas como 1 (pelo menos uma é necessária).
#     antenas = 1
    
#     # Inicialize o ponto médio entre as casas.
#     meio = 0
    
#     for i in range(1, len(localizacao_casa)):
        
#         # Se a distância entre a casa atual e a casa anterior for menor ou igual ao alcance da antena.
#         if (localizacao_casa[i] - primeira_casa) <= alcance_transmissor:
            
#             # Atualize o ponto médio.
#             meio = localizacao_casa[i]
            
#         # Se a distância entre a casa atual e o ponto médio não estiver dentro do alcance da antena.
#         if not localizacao_casa[i] - meio <= alcance_transmissor:
            
#             # Adicione outra antena.
#             antenas += 1
            
#             # Atualize a localização da antena.
#             primeira_casa = localizacao_casa[i]
            
#     # Retorna o número mínimo de antenas necessárias.
#     return antenas


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Ordena as localizações das casas.
#     localizacao_casa.sort()
    
#     # Índice atual.
#     i = 0
    
#     # Posição inicial para o primeiro transmissor.
#     pos = localizacao_casa[0]
    
#     # Inicialmente, temos pelo menos um transmissor.
#     resultado = 1
    
#     # Itera pelas casas para encontrar a melhor localização para os transmissores.
#     for j in range(1, len(localizacao_casa)):
        
#         # Se a casa atual está dentro do alcance do transmissor atual.
#         if localizacao_casa[j] - localizacao_casa[i] <= alcance_transmissor:
            
#             # Atualiza a posição para a casa atual.
#             pos = localizacao_casa[j]
            
#         # Se a casa atual não está no alcance do transmissor atual, mas no alcance de um novo.
#         elif localizacao_casa[j] - pos <= alcance_transmissor: 
            
#             # Avança para a próxima casa.
#             continue
        
#         else:
            
#             # Atualiza o índice para a casa atual.
#             i = j 
            
#             # Atualiza a posição para a casa atual.
#             pos = localizacao_casa[j]
            
#             # Incrementa o número de transmissores necessários.
#             resultado += 1
    
#     # Retorna o número mínimo de transmissores necessários.
#     return resultado


# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Obtém o tamanho da lista localizacao_casa
#     n = len(localizacao_casa)
    
#     # Ordena a lista localizacao_casa em ordem crescente
#     localizacao_casa.sort()
    
#     # Inicializa o contador e o índice
#     contador, índice = 0,0
    
#     # Inicia um loop enquanto índice for menor que n
#     while(índice < n):
        
#         # Incrementa o contador contador
#         contador += 1
        
#         # Define a posição da primeira casa a ser coberta pelo transmissor
#         primeira_casa = localizacao_casa[índice] + alcance_transmissor
        
#         # Armazena o valor atual de i em j
#         j = índice
        
#         # Enquanto índice for menor que n e o valor da casa em localizacao_casa[índice] for menor ou igual a primeira_casa
#         while índice < n and localizacao_casa[índice] <= primeira_casa:
            
#             # Incrementa i
#             índice += 1
            
#         # Verifica se o intervalo entre j e índice é igual a 1 (uma casa)
#         if j == índice + 1:
            
#             # Se for, continua para a próxima iteração
#             continue
        
#         # Calcula a posição do meio entre as casas em j-1 e i-1
#         meio = localizacao_casa[índice - 1] + alcance_transmissor
        
#         # Enquanto i for menor que n e o valor da casa em localizacao_casa[i] for menor ou igual a meio
#         while índice < n and localizacao_casa[índice] <= meio:
            
#             # Incrementa i
#             índice += 1
            
#     # Retorna o valor do contador c
#     return contador


# # Importa a função bisect_right da biblioteca bisect
# from bisect import bisect_right

# def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
#     # Ordena a lista localizacao_casa em ordem crescente
#     localizacao_casa.sort()
    
#     # Inicializa o resultado como 0
#     resultado = 0
    
#     # Obtém o tamanho da lista localizacao_casa
#     n = len(localizacao_casa)
    
#     # Inicializa o índice i como 0
#     i = 0
    
#     # Inicia um loop enquanto i for menor que n
#     while (i < n):
        
#         # Encontra o índice onde a localização casa excede o alcance do transmissor
#         arr = bisect_right(localizacao_casa, localizacao_casa[i] + alcance_transmissor)
        
#         # Incrementa o resultado em 1, pois é necessário um transmissor
#         resultado += 1 
        
#         # Encontra o próximo índice onde o transmissor pode ser colocado
#         i = bisect_right(localizacao_casa, localizacao_casa[arr - 1] + alcance_transmissor)
        
#     # Retorna o resultado final
#     return resultado

def hackerlandRadioTransmitters(localizacao_casa, alcance_transmissor):
    
    # Classifica as localizações das casas em ordem crescente.
    localizacao_casa.sort()
    
    # Inicializa a posição da primeira casa menos 2 vezes o alcance do transmissor.
    pos = localizacao_casa[0] - 2 * alcance_transmissor
    
    # Inicializa o contador para o número de transmissores.
    contador = 0
    
    # Itera sobre as localizações das casas.
    for i in localizacao_casa:
        
        # Verifica se a diferença entre a posição atual e a posição anterior é maior que o alcance do transmissor.
        if abs(i - pos) > alcance_transmissor:
            
            # Inicializa um contador auxiliar.
            j = 0
            
            # Procura a casa mais distante que possa ser coberta pelo transmissor.
            while j <= alcance_transmissor:
                
                # Se uma casa dentro do alcance for encontrada
                if i + alcance_transmissor - j in localizacao_casa:
                    
                    # atualiza a posição do transmissor
                    pos = i + alcance_transmissor - j 
                    
                    # e incrementa o contador.
                    contador += 1
                    
                    break
                
                j += 1
    
    # Retorna o número de transmissores necessários.
    return contador