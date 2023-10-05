# Neste problema, você está jogando um jogo chamado 
# "Tower Breakers". O jogo é jogado com as seguintes regras:

# Existem n torres, numeradas de 1 a n.
# Cada torre tem uma altura m.
# Dois jogadores jogam alternadamente.
# Em cada turno, um jogador escolhe uma torre com altura m > 1 e 
# reduz a altura da torre para m - 1. O jogador que não consegue 
# fazer um movimento perde o jogo.
# A tarefa é determinar o vencedor do jogo com base nas alturas 
# iniciais das torres. Você precisa escrever uma função ou programa 
# que, dado o número de torres e as alturas iniciais das torres, 
# determine se o primeiro jogador (jogador 1) ou o segundo jogador 
# (jogador 2) ganhará o jogo se ambos jogarem de forma otimizada. 
# Neste problema, você está jogando um jogo chamado "Tower Breakers". 
# O jogo é jogado com as seguintes regras:

# Existem n torres, numeradas de 1 a n.
# Cada torre tem uma altura m.
# Dois jogadores jogam alternadamente.
# Em cada turno, um jogador escolhe uma torre com altura m > 1 
# e reduz a altura da torre para m - 1. O jogador que não consegue 
# fazer um movimento perde o jogo.
# A tarefa é determinar o vencedor do jogo com base nas alturas 
# iniciais das torres. Você precisa escrever uma função ou programa 
# que, dado o número de torres e as alturas iniciais das torres, 
# determine se o primeiro jogador (jogador 1) ou o segundo jogador 
# (jogador 2) ganhará o jogo se ambos jogarem de forma otimizada.


# Define uma função chamada towerBreakers que 
# recebe dois argumentos: n (número de torres) e m (altura das torres).

def towerBreakers(n, m):
    
    # Se a altura das torres for igual a 1, o jogador 2 sempre ganha imediatamente.
    # Caso contrário, a lógica para determinar o vencedor é baseada no número de torres (n).
    # Se o número de torres for ímpar, o jogador 1 ganha, caso contrário, o jogador 2 ganha.
    # Isso é feito subtraindo 1 se n for ímpar, o que resulta em 2 para n par ou 1 para n ímpar.
    return 2 if m == 1 else 2 - (n % 2)