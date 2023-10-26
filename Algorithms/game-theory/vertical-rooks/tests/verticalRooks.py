# Neste problema, você é apresentado a um jogo de rooks vertical entre dois jogadores, onde o objetivo é forçar o oponente a ficar em uma posição perdedora. Um rook é uma peça de xadrez que se move vertical ou horizontalmente. Cada jogador controla uma coluna de rooks, e eles se alternam fazendo movimentos em uma coluna, removendo um rook por vez.

# A tarefa é determinar qual jogador vencerá o jogo, supondo que ambos joguem de forma ótima. O jogador que faz o último movimento vencedor é declarado vencedor.

# Dois jogadores, que chamaremos de jogador 1 e jogador 2, competem em um jogo com várias colunas de torres (rooks).

# Cada jogador tem controle sobre um conjunto de colunas de torres. As colunas de torres são representadas por números inteiros de 1 a N.

# Em cada jogada, um jogador pode escolher uma coluna de torres que controla e mover uma torre para outra coluna controlada por ele. A torre pode ser movida para qualquer posição na coluna de destino.

# O jogador que fizer o último movimento vencedor é declarado o vencedor.

# A tarefa é determinar qual jogador vencerá o jogo, supondo que ambos joguem de forma ótima.

def verticalRooks(r1, r2):
    
    # Inicializa uma variável para calcular os XORs
    xors = 0
    
    # Itera sobre as listas r1 e r2, que representam as posições das torres em colunas controladas por player-1 e player-2
    for y1, y2 in zip(r1, r2):
        
        # Calcula a diferença absoluta entre as posições y1 e y2 e subtrai 1
        # Isso representa a quantidade de movimentos necessários para alinhar as torres
        # Adiciona o resultado ao cálculo dos XORs
        xors ^= (abs(y1 - y2) - 1)
    
    # Se o resultado dos XORs for diferente de zero, retorna "player-2", caso contrário, retorna "player-1"
    return "player-2" if xors != 0 else "player-1"