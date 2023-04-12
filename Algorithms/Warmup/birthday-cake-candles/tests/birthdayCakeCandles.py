# def birthdayCakeCandles(candles):
    
#     return (candles.count(max(candles)))


def birthdayCakeCandles(candles):
    
    # Começamos considerando a primeira vela como a maior
    grande = candles[0]
    # Inicializamos a contagem com zero
    contar = 0
    
    # Percorremos a lista de velas
    for i in candles:
        
        # Se encontrarmos uma vela maior que a maior atual, atualizamos as variáveis grande e contar
        if i > grande:
            
            grande = i
            # Reiniciamos a contagem, já que encontramos uma vela maior
            contar = 1
        
         # Se encontrarmos uma vela igual à maior atual, incrementamos a contagem
        elif i == grande:
            
            contar += 1
     # Retornamos a contagem de velas maiores ou iguais à maior vela
    return contar

if __name__ == "__main__":
    
    contagem_de_velas = int(input().strip())
    
    velas = list(map(int, input().rstrip().split()))
    
    resultado = birthdayCakeCandles(velas)
    
    print(str(resultado) + '\n')