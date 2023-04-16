# Uma prisão tem vários prisioneiros e várias guloseimas para distribuir a eles. 
# O carcereiro decide que a maneira mais justa de dividir as guloseimas é sentar 
# os prisioneiros em torno de uma mesa circular em cadeiras numeradas sequencialmente. 
# Um número de cadeira será sorteado de um chapéu. Começando com o prisioneiro naquela cadeira, 
# um doce será entregue a cada prisioneiro sequencialmente ao redor da mesa até que todos tenham sido distribuídos.

# O carcereiro está brincando, no entanto. O último pedaço de doce se parece com todos os outros, 
# mas tem um gosto horrível . Determine o número da cadeira ocupada pelo prisioneiro que receberá aquele doce.

# n numero_prisioneiros
# m numero_doces
# s primeira_cadeira_distribuir

def saveThePrisoner(numero_prisioneiros, numero_doces, primeira_cadeira_distribuir):
    
    # Calcula a posição do prisioneiro que irá receber o último doce
    # A operação % (resto da divisão) é utilizada para garantir que a posição não ultrapasse o número de prisioneiros
    
    # primeira_cadeira_distribuir - 1: subtrai 1 da posição da primeira cadeira para que possamos usar a indexação baseada em zero 
    # (ou seja, se a primeira cadeira é 1, isso tornaria a posição da primeira cadeira 0).
    
    # numero_doces % numero_prisioneiros: encontra o resto da divisão de numero_doces pelo número de prisioneiros, para garantir que 
    # não distribuamos mais doces do que prisioneiros
    
    # primeira_cadeira_distribuir - 1 + numero_doces % numero_prisioneiros: soma o resultado do passo anterior ao número de 
    # cadeiras distribuídas. Isso nos dá o índice do último prisioneiro a quem um doce é dado.
    
    # (primeira_cadeira_distribuir - 1 + numero_doces % numero_prisioneiros) % numero_prisioneiros: se houver mais doces do que prisioneiros, 
    # isso nos permitirá começar de novo a partir do primeiro prisioneiro. Aqui, usamos o operador % para calcular o resto da divisão do índice 
    # encontrado no passo anterior pelo número total de prisioneiros.
    
    # numero_prisioneiros if posicao == 0 else posicao: verifica se o prisioneiro encontrado no passo anterior é o último prisioneiro na fila. 
    # Se sim, retornamos numero_prisioneiros. Caso contrário, retornamos a posição do prisioneiro.
    posicao = (primeira_cadeira_distribuir - 1 + numero_doces % numero_prisioneiros)  % numero_prisioneiros
    
    # Verifica se o prisioneiro encontrado foi o último da fila. 
    # Se for o caso, retorna o número de prisioneiros para indicar que o último prisioneiro recebeu o último doce
    return numero_prisioneiros if posicao == 0 else posicao


# def saveThePrisoner(numero_prisioneiros, numero_doces, primeira_cadeira_distribuir):
    
#     # a expressão (numero_doces - 1) + (primeira_cadeira_distribuir - 1) 
#     # calcula a posição do último prisioneiro que recebe o doce
#     # o operador % (numero_prisioneiros) 
#     # garante que o número retornado esteja dentro do intervalo de prisioneiros (1 a numero_prisioneiros)
#     return ((numero_doces - 1) + (primeira_cadeira_distribuir - 1)) % numero_prisioneiros + 1

# def saveThePrisoner(n, m, s):
    
#     # Encontra o prisioneiro que receberá o último doce.
#     prisioneiro = (m + (s-1)) % n
    
#     # Se o prisioneiro encontrado for 0
#     if prisioneiro == 0:
        
#         # então o último prisioneiro a receber doce será o número de prisioneiros n.
#         return n
				
#     return prisioneiro 

if __name__ ==  "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    numero_prisioneiros = int(primeira_multipla_entrada[0])
    numero_doces = int(primeira_multipla_entrada[1])
    primeira_cadeira_distribuir = int(primeira_multipla_entrada[2])
    
    resultado = saveThePrisoner(numero_prisioneiros, numero_doces, primeira_cadeira_distribuir)
    
    print(str(resultado) + '\n')