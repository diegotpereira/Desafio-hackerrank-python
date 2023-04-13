# bill custo de cada item
# k é o indice que mostra o que Ana não comeu
# b a quantidade de dinheiro que Ana contribuiu

# def bonAppetit(bill, k, b):
    
#     # calcula o valor total da conta dividida igualmente entre Ana e Brian
#     total_cada_item = sum(bill)
    
#     # calcula quanto Ana deve pagar (excluindo o item que ela não comeu)
#     ana_deve = (total_cada_item - bill[k]) / 2
    
#     # valor que Ana pagou
#     ana_pagou = b 
    
#     if (ana_deve == ana_pagou):
        
#         # se o valor que Ana pagou está correto, retorna "Bon Appetit"
#         return("Bon Appetit")
        
#     if (ana_deve < ana_pagou):
        
#         # se Ana pagou mais do que deveria, retorna a diferença
#         return(int(ana_pagou - ana_deve))
    

# def bonAppetit(bill, k, b):
    
#     # Retorna "Bon Appetit" se a diferença entre o valor pago e a quantidade que Anna deve pagar for zero,
#     # caso contrário retorna a diferença arredondada para inteiro.
#     return ("Bon Appetit" if b - ((sum(bill) - bill[k]) / 2) == 0 else int(b - ((sum(bill) - bill[k]) / 2)))


def bonAppetit(bill, k, b):
    
    # Remove o item não consumido pela Ana da lista
    bill.pop(k)
    
    # Calcula a parte da Ana do valor total da conta dividida igualmente
    parte_da_ana = sum(bill) / 2
    
     # Verifica se a Ana pagou a quantia correta
    if b == parte_da_ana:
        
        return ('Bon Appetit')
    
    else:
        
        # Caso contrário, retorna o valor da diferença em formato inteiro.
        return (int(b - parte_da_ana))

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()

    n = int(primeira_multipla_entrada[0])

    k = int(primeira_multipla_entrada[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    resultado = bonAppetit(bill, k, b)
    
    print(resultado)