# O problema envolve um jogo entre Bob e Ben, que ocorre em uma 
# floresta composta por várias árvores. Aqui estão as regras do jogo:

# O jogo começa com uma floresta de árvores.
# Bob sempre começa a jogar e eles alternam os turnos.
# O primeiro jogador que não tiver movimentos disponíveis perde o jogo.
# Durante cada movimento, o jogador remove um nó. Se o nó não for uma 
# folha, a árvore inteira desaparece; caso contrário, o restante da 
# árvore permanece na floresta. Uma folha é definida como um nó com 
# exatamente uma aresta conectada.
# Ambos os jogadores jogam de forma otimizada, o que significa que 
# eles não farão um movimento que os leve a perder o jogo se houver 
# um movimento melhor e vencedor disponível.
# Cada árvore na floresta é definida por dois valores: o número de 
# nós na árvore (n) e uma constante (k). Os nós são numerados de 1 a n, 
# e as arestas são numeradas de 1 a n-1.

# O objetivo do problema é determinar quem vencerá o jogo com base nos 
# valores de n e k para cada árvore na floresta.

# O formato de entrada inclui o número de jogos (testes) e, para cada 
# jogo, o número de árvores na floresta, seguido pelos valores de n e k para cada árvore.

# A saída deve indicar quem vencerá o jogo (Bob ou Ben) para cada jogo.


# Função que determina se um número de nós é "suj0" (não uma folha)

def numeroSujo(nodes):
    
    # Se o número de nós for 0 ou 2, retorna 0 (não sujo)
    if (nodes == 0  or nodes == 2):
        
        return 0
    
    # Caso contrário, calcula o valor com base no número de nós
    else:
        
        return ((nodes - 1) % 2 + 1)
    
# Função principal que determina o vencedor do jogo Bob and Ben com base nas árvores
def bobAndBen(arvores):
    
    # Lista para armazenar se cada árvore é "suj0" ou não
    numerosSujos = []
    
    # Calcula se cada árvore é "suj0" ou não e armazena na lista
    for i in range(len(arvores)):
        
         # Inicializa o resultado com o primeiro valor
        numerosSujos.append(numeroSujo(arvores[i][0]))
        
    # Inicializa o resultado com o primeiro valor
    re = numerosSujos[0]
    
    # Verifica se há mais de uma árvore (mais de um valor em numerosSujos)
    if((len(numerosSujos)-1) > 1):
        
        # Realiza uma operação de XOR (bitwise) em todos os valores de numerosSujos
        for j in range(1, len(numerosSujos)):
            
            re ^= numerosSujos[j]
            
    # Caso haja exatamente duas árvores, calcula o resultado com base nos dois valores
    elif((len(numerosSujos) - 1) == 1):
        
        re = re ^numerosSujos[1]
        
     # Verifica se o resultado final é diferente de 0
    if (re != 0):
        
        # Bob vence o jogo
        return 'BOB'
    
    else:
        
        # Ben vence o jogo
        return 'BEN'
    
    