# O problema "Alice and Bob's Silly Game" 
# no HackerRank é um desafio relacionado 
# a um jogo simples entre Alice e Bob. 
# A tarefa é a seguinte:

# Alice e Bob estão jogando um jogo com pedras. 
# O jogo é jogado da seguinte maneira:

# Inicialmente, há uma pilha de pedras.
# Os jogadores alternam, com Alice indo primeiro.
# Em cada turno, um jogador pode remover qualquer 
# quantidade de pedras da pilha, pelo menos uma 
# pedra deve ser removida.
# O jogador que não consegue fazer um movimento 
# válido perde o jogo.
# A tarefa é determinar quem ganha o jogo com base 
# no número inicial de pedras na pilha. Você deve 
# escrever um programa que, dado o número inicial 
# de pedras, determine se Alice ou Bob ganha o jogo 
# se ambos jogarem de forma ótima.

def sillyGame(n):
    
    # Função para verificar se um número é primo
    def eh_primo(num):
        
        # Verifica se o número é menor que 2 (não é primo)
        if num < 2:
            
            return 0
        
        # Inicializa uma lista de peneira para marcar números compostos
        peneira = [True] * (num + 1)
        
        # Define 0 e 1 como não primos
        peneira[0] = peneira[1] = False 
        
        # Itera por todos os números até a raiz quadrada de 'num'
        for p in range(2, int(num ** 0.5) + 1):
            
            if peneira[p]:
                
                # Marca todos os múltiplos de 'p' como números compostos
                for i in range(p * p, num + 1, p):
                    
                    peneira[i] = False
                    
        # Conta quantos números primos existem até 'num'
        return sum(1 for primo in peneira if primo)
    
    # Chama a função para contar números primos até 'n'
    contar_primo = eh_primo(n)
    
    # Verifica se o número de primos é ímpar ou par
    if contar_primo % 2 == 1:
        
        # Se for ímpar, Alice ganha
        return 'Alice'
    
    else:
        
        # Se for par, Bob ganha
        return 'Bob'
    
    # minha_lista = [1] * (n + 1)
    # minha_lista[0] = 0
    
    # for i in range(2, int(n ** 0.5) + 1):
        
    #     if minha_lista[i] == 1:
            
    #         for j in range(i * i, n + 1, i):
                
    #             minha_lista[j] = 0
    
    # return minha_lista