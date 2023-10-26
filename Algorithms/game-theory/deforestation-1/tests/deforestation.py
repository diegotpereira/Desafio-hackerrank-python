# A tarefa do problema é determinar o vencedor de um jogo 
# jogado em uma árvore enraizada. A árvore tem vértices 
# numerados e o primeiro vértice (1) é sempre a raiz. 
# Aqui estão as regras básicas do jogo:

# Os jogadores (Alice e Bob) alternam seus turnos e 
# sempre fazem movimentos ótimos.
# Durante cada jogada, um jogador remove uma aresta 
# da árvore, desconectando uma das folhas ou ramos. 
# A folha ou ramo que foi desconectado da árvore é removido do jogo.
# O primeiro jogador a ficar sem movimentos perde o jogo.
# Alice sempre faz a primeira jogada.
# O objetivo do problema é determinar se Alice ou Bob 
# vence o jogo, com base na estrutura da árvore e nas 
# regras acima. Se Alice vencer, você deve imprimir 
# "Alice"; caso contrário, imprima "Bob".

# A entrada do problema consiste no número de casos 
# de teste, seguido pelos detalhes de cada caso de 
# teste. Cada caso de teste começa com o número de 
# nós na árvore e, em seguida, há linhas subsequentes 
# que representam as arestas da árvore, conectando pares de nós.

def deforestation(n, arvore):
    
    # Crie um dicionário para representar a árvore como um grafo.
    dicionario = dict()
    
    # Preencha o dicionário com as conexões entre nós da árvore.
    for x in arvore:
        
        if x[0] in dicionario:
            
            dicionario[x[0]].add(x[1])
            
        else:
            
            dicionario[x[0]] = set()
            dicionario[x[0]].add(x[1])
            
        if x[1] in dicionario:
            
            dicionario[x[1]].add(x[0])
            
        else:
            
            dicionario[x[1]] = set()
            dicionario[x[1]].add(x[0])
            
    # Crie uma lista 'dp' para armazenar os resultados intermediários da função recursiva.
    lista = [-1 for i in range(n + 1)]
    
    # Defina a função recursiva 'r' para determinar o vencedor do jogo.
    def recursiva(node, prev):
        
        if lista[node] == -1:
            
            lista[node] = 1
            
            contador = 0
            
            tmp = []
            
            # Verifique os nós vizinhos do nó atual.
            if node in dicionario:
                
                for x in dicionario[node]:
                    
                    if x != prev:
                        
                        tmp.append(1 + recursiva(x, node))
                        
            # Realize operações XOR em 'tmp' para calcular a condição de vitória.
            for x in tmp:
                
                contador ^= x 
                
            return contador 
        
        else:
            
            return 0
            
    # Chame a função recursiva para calcular o resultado final do jogo.
    contador = recursiva(1, -1)
    
    # Determine o vencedor com base no resultado 'contador'.
    if contador == 0:
        
        return 'Bob'
    
    return "Alice"