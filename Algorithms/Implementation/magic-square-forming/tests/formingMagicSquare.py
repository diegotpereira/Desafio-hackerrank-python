# quadrados = [
#     [[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
#     [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
#     [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
#     [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
#     [[4, 9, 2], [3, 5, 7], [8, 1, 6]], 
#     [[8, 3, 4], [1, 5, 9], [6, 7, 2]], 
#     [[6, 1, 8], [7, 5, 3], [2, 9, 4]], 
#     [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# ]

# def formingMagicSquare(s):
    
#     # cria uma lista vazia para armazenar os custos de cada quadrado mágico
#     custos=[]
    
#     # itera sobre todos os quadrados mágicos possíveis
#     for q in quadrados:
        
#         # inicializa o custo como zero
#         custo=0
        
#         # itera sobre cada linha da matriz s e do quadrado mágico q
#         for i in range(3):
            
#             # itera sobre cada coluna da matriz s e do quadrado mágico q
#             for j in range(3):
                
#                 # calcula o custo de transformar o elemento s[i][j] em q[i][j]
#                 custo+=abs(q[i][j]-s[i][j])
                
#         # adiciona o custo do quadrado mágico q à lista de custos
#         custos.append(custo)
        
#     # retorna o menor custo encontrado entre todos os quadrados mágicos possíveis
#     return min(custos)


# def formingMagicSquare(s):
    
#     # inicializa o custo como zero
#     custo = 0
    
#     # define o primeiro quadrado mágico possível
#     b1 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    
#     # define o segundo quadrado mágico possível
#     b2 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    
#     # define o terceiro quadrado mágico possível
#     b3 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    
#     # define o quarto quadrado mágico possível
#     b4 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    
#     # define o quinto quadrado mágico possível
#     b5 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    
#     # define o sexto quadrado mágico possível
#     b6 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    
#     # define o sétimo quadrado mágico possível
#     b7 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    
#     # define o oitavo quadrado mágico possível
#     b8 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    
#     # armazena todos os quadrados mágicos 
#     base_linha = [b1, b2, b3, b4, b5, b6, b7, b8]
    
#      # itera sobre cada linha da matriz s
#     for i in range(3):
        
#         # itera sobre cada coluna da matriz s
#         for j in range(3):
            
#             # calcula o custo de transformar o elemento s[i][j] no elemento correspondente do primeiro quadrado mágico possível
#             custo += abs(s[i][j] - base_linha[0][i][j])
            
#     # itera sobre todos os quadrados mágicos possíveis, exceto o primeiro
#     for a in base_linha[1::]:
        
#         # inicializa o custo temporário como zero
#         custo_temporario = 0
        
#         # itera sobre cada linha da matriz s
#         for i in range(3):
            
#             # itera sobre cada coluna da matriz s
#             for j in range(3):
                
#                 # calcula o custo de transformar o elemento s[i][j] no elemento correspondente do quadrado mágico atual
#                 custo_temporario += abs(s[i][j] - a[i][j])
                
#         # se o custo temporário for menor ou igual ao custo atual
#         if custo_temporario <= custo:
            
#             # atualiza o custo atual com o custo temporário
#             custo = custo_temporario
                
#     # retorna o menor custo encontrado entre todos os quadrados mágicos possíveis
#     return custo

    
if __name__ == "__main__":
    
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    resultado = formingMagicSquare(s)

    print(str(resultado) + '\n')