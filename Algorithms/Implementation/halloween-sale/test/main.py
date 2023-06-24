from howManyGames import howManyGames

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    # int p: o preço do primeiro jogo
    # int d: o desconto do preço do jogo anterior
    # int m: o custo mínimo de um jogo
    # int s: o orçamento inicial
    
    preco_primeiro_jogo = int(primeira_multipla_entrada[0])
    desconto_jogo_anterior = int(primeira_multipla_entrada[1])
    custo_minimo_jogo = int(primeira_multipla_entrada[2])
    orcamento_inicial = int(primeira_multipla_entrada[3])
    
    resultado = howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial)
    
    print(str(resultado) + '\n')