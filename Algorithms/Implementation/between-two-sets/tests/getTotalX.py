# objetivo encontrar todos os inteiros que são múltiplos de todos os 
# elementos da primeira lista a e que também dividem todos os elementos da segunda lista b.

def getTotalX(a, b):
        
    # Define uma variável para armazenar o número de valores em comum entre a e b
    contar = 0
    
    # Loop que itera pelos valores entre o maior número em a e o menor número em b
    for i in range(max(a), min(b) + 1):
        
         # Define uma variável booleana como verdadeira
        div = True
            
        # Loop que itera pelos valores em a e verifica se o valor i é divisível por cada um desses valores
        for j in a:
            
            # Se i não for divisível por j, a variável div se torna falsa
            if i % j != 0: div = False 
            
        # Loop que itera pelos valores em b e verifica se cada um desses valores é divisível por i
        for j in b:
            
            # Se j não for divisível por i, a variável div se torna falsa
            if j % i != 0: div = False
            
         # Se a variável div for verdadeira, incrementa a variável contar
        if div: contar += 1
       
    # Retorna o valor final de contar, representando o número de valores em comum entre a e b 
    return contar

# def getTotalX(a, b):
    
#     # Inicializa o contador de números entre os arrays como 0
#     contar = 0
    
#     # Percorre todos os inteiros entre o maior número do array a e o menor número do array b
#     for i in range(a[-1], b[0] + 1):
        
#         # Inicializa a flag que indica se o número atual é um fator comum como 0
#         flag = 0
        
#         # Verifica se todos os elementos do array a são fatores do número atual
#         for j in a:
            
#             # Se o resto da divisão não for 0, o número atual não é um fator comum
#             if i % j != 0:
                
#                 # Seta a flag para 1 para indicar que o número atual não é um fator comum
#                 flag = 1
                
#         # Se a flag não tiver sido alterada para 1, todos os elementos do array a são fatores do número atual                
#         if flag != 1:
            
#             # Verifica se o número atual é um fator comum de todos os elementos do array b
#             for k in b:
                
#                 # Se o resto da divisão não for 0, o número atual não é um fator comum
#                 if k % i != 0:
                    
#                      # Seta a flag para 1 para indicar que o número atual não é um fator comum
#                     flag = 1
                    
#         # Se a flag não tiver sido alterada para 1, o número atual é um fator comum de todos os elementos de a e b
#         if flag == 0:
            
#             # Incrementa o contador de números entre os arrays em 1
#             contar += 1
        
#     # Retorna o contador final de números entre os arrays
#     return contar

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    m = int(primeira_multipla_entrada[1])
    
    arr = list(map(int, input().rstrip().split()))
    
    brr = list(map(int, input().rstrip().split()))
    
    total = getTotalX(arr, brr)
    
    print(str(total) + '\n')