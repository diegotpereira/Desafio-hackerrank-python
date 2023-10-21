
# A tarefa é determinar o número de maneiras diferentes 
# que dois astronautas de países diferentes podem ser selecionados para a mesma missão lunar.

# def journeyToMoon(n, astronauta):
    
#     # Crie um conjunto inicial de agrupamentos, onde cada astronauta é seu próprio grupo.
#     agrupamentos = [set([i]) for i in range(n)]
    
#     # Combine os agrupamentos com base nas informações fornecidas pelos astronautas.
#     for p in astronauta:
        
#         # Encontre todos os astronautas relacionados a partir dos agrupamentos existentes.
#         tudo_relacionado = agrupamentos[p[0]].union(agrupamentos[p[1]])
        
#         # Atualize os agrupamentos de astronautas relacionados.
#         for i in tudo_relacionado:
            
#             agrupamentos[i] = tudo_relacionado
    
#     # Converta os agrupamentos em um conjunto de tuplas para eliminar duplicatas.
#     agrupamentos = set([tuple(s) for s in agrupamentos])
    
#     # Inicialize as variáveis 's' e 's2' para calcular o número de pares de astronautas.
#     s, s2 = 0, 0
    
#     # Calcule 's' como a soma do tamanho de cada agrupamento e 's2' como 
#     # a soma dos quadrados dos tamanhos dos agrupamentos.
#     for c in agrupamentos:
        
#         s += len(c)
#         s2 += len(c) ** 2
        
#     # Calcule o número de pares possíveis de astronautas que não são da mesma nacionalidade
#     # subtraindo o quadrado de 's' do valor de 's2' e dividindo por 2.
#     return (s ** 2 - s2) // 2


# def journeyToMoon(n, astronauta):
    
#     # Inicialize uma lista 'lista' que conterá grupos iniciais com um astronauta em cada grupo.
#     lista = []
    
#     for i in range(n):
        
#         lista.append([i])
        
#     # Combine os grupos com base nas informações fornecidas pelos astronautas.
#     for a in astronauta:
        
#         ind1 = lista[a[0]][0]
#         ind2 = lista[a[1]][0]
        
#         # Se o índice do primeiro astronauta é menor que o índice do segundo astronauta,
#         if ind1 < ind2:
            
#             # estenda o grupo do segundo astronauta e atualize os índices dos astronautas no primeiro grupo.
#             lista[ind2].extend(lista[ind1])
            
#             for t in lista[ind1]:
                
#                 lista[t][0] = ind2
                
#         # Se o índice do primeiro astronauta é maior que o índice do segundo astronauta,
#         elif ind1 > ind2:
            
#             # estenda o grupo do primeiro astronauta e atualize os índices dos astronautas no segundo grupo.
#             lista[ind1].extend(lista[ind2])
            
#             for t in lista[ind2]:
                
#                 lista[t][0] = ind1
                
#     # Crie uma nova lista 'lista2' que contém apenas grupos em que o índice do primeiro astronauta é igual ao índice do grupo.
#     lista2 = [lista[i] for i in range(n) if lista[i][0] == i]
    
#     total = 0
    
#     # Calcule o número total de pares de astronautas que não são da mesma nacionalidade
#     for i in lista2:
        
#         n -= len(i)
        
#         total += n * len(i)
        
#     return total

def journeyToMoon(n, astronauta):
    
    # Cria dicionários para rastrear nós visitados 
    # e conexões entre astronautas.
    visitado = {}
    grafico = {}
    
    # Inicializa os dicionários para todos os nós 
    # e os marca como não visitados.
    for i in range(n):
        
        # Cria uma lista vazia para as conexões do astronauta i.
        grafico[i] = []
        
        # Marca o astronauta i como não visitado.
        visitado[i] = False
        
    # Preenche o grafo com as conexões fornecidas pelos astronautas.
    for i in astronauta:
        
        # Adiciona o astronauta i[1] às conexões de i[0].
        grafico[i[0]] = grafico[i[0]] + [i[1]]
        
        # Adiciona o astronauta i[0] às conexões de i[1].
        grafico[i[1]] = grafico[i[1]] + [i[0]]
    
    # Inicializa listas para armazenar grupos e contagens.
    # Lista de grupos de astronautas.
    grupo = []
    
    # Lista de contagens para cada grupo.
    contador = []
    
    # Percorre todos os nós para formar grupos.
    for i in range(n):
        
        # se ainda não foi visitado
        if visitado[i] == False:
            
            # Inicializa um novo grupo com o astronauta i.
            grupo.append([i])
            
            # Inicializa a contagem do grupo como 1.
            contador.append(1)
            
            # Marca o astronauta i como visitado.
            visitado[i] = True
            
            # Inicializa uma fila com o astronauta i.
            fila = [i]
            
            # Explora os nós conectados a partir do nó atual
            while len(fila) > 0:
                
                # Obtém o nó no início da fila.
                raiz = fila[0]
                
                # Remove o nó da fila.
                fila.pop(0)
                
                # Obtém as conexões do nó raiz.
                nos = grafico[raiz]
                
                for i in range(len(nos)):
                    
                    # Percorre os nós conectados a partir do nó atual.
                    if visitado[nos[i]] == False:
                        
                         # Adiciona o nó à lista de astronautas do grupo.
                        grupo[-1].append(nos[i])
                        
                        # Aumenta a contagem do grupo.
                        contador[-1] += 1
                        
                        # Marca o nó como visitado.
                        visitado[nos[i]] = True 
                        
                        # Adiciona o nó à fila para exploração.
                        fila.append(nos[i])
                        
                        
    # Calcula a soma total das contagens para determinar o resultado. 
    
    # Variável para rastrear a soma das contagens.        
    soma = 0
    
    # Variável para armazenar o resultado final.
    resultado = 0
    
    # Percorre a lista de contagens para cada grupo.
    for i in contador:
        
        # Atualiza o resultado com base na soma atual e a contagem do grupo.
        resultado += soma * i 
        
        # Atualiza a soma com a contagem atual.
        soma += i                 
                
    # Retorna o resultado final.
    return resultado