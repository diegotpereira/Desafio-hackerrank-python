# O problema apresentado envolve encontrar o teclado e o USB drive mais caros que podem ser comprados com um orçamento dado. 
# Para resolver esse problema, é necessário seguir os seguintes passos:

# Ler os valores de entrada que contêm o orçamento, os preços dos teclados e os preços dos USB drives.
# Percorrer todos os pares possíveis de teclado e USB drive e verificar se o preço total é menor ou igual ao orçamento.
# Se o preço total for menor ou igual ao orçamento e maior do que o preço máximo atual, atualizar o preço máximo.
# Retornar o preço máximo atual se ele for maior do que zero, caso contrário, retornar -1 para indicar que não é possível 
# comprar ambos os itens com o orçamento dado.
# Segue abaixo um exemplo de código em Python que implementa essa lógica:


# def getMoneySpent(teclados, dispositivos, orcamento):
    
#     # Inicializa a variável soma com 0 e impossible com -1
#     soma  = 0
#     impossible = -1
    
#     # Percorre todos os teclados e todos os dispositivos
#     for i in teclados:
        
#         for j in dispositivos:
            
#             # Verifica se a soma dos preços é maior do que a soma atual e menor ou igual ao orçamento disponível
#             if i + j > soma and i + j <= orcamento:
                
#                 # Atualiza a soma com o novo valor
#                 soma = i + j
                
#     # Verifica se foi possível comprar algum item, caso contrário, retorna impossible
#     if soma == 0:
        
#         return impossible
    
#     else:
        
#         return soma 


def getMoneySpent(teclados, dispositivos, orcamento):
    
    # Inicializa a variável custo com 0
    custo = 0
    
    # Percorre todos os teclados e todos os dispositivos
    for i in teclados:
        
        for j in dispositivos:
            
            # Verifica se a soma dos preços é menor ou igual ao orçamento disponível e maior do que o custo atual
            if (i + j) <= orcamento and (i + j) > custo:
                
                # Atualiza o custo com o novo valor
                custo = (i + j)
                
                
    # Verifica se foi possível comprar algum item, caso contrário, retorna -1
    if custo == 0:
        
        return - 1
    
    else:
        
        return custo
    
    
    # print(teclados) # [3, 1]
    # print(dispositivos) # [5, 2, 8]
    # print(orcamento) # 10
    # return 

if __name__ == "__main__":
    
    bnm = input().split()

    orcamento = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    teclados = list(map(int, input().rstrip().split()))

    dispositivos = list(map(int, input().rstrip().split()))
    
    #
    # A quantia máxima de dinheiro que ela pode gastar em um teclado e unidade USB, ou -1 se ela não puder comprar os dois itens
    #
    
    
    dinheiro_gasto = getMoneySpent(teclados, dispositivos, orcamento)

    print(str(dinheiro_gasto) + '\n')