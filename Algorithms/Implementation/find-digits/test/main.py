from findDigits import findDigits

if __name__ == "__main__":
    
    # Lê o número de casos de teste
    t = int(input().strip())
    
     # Executa o loop para cada caso de teste
    for tItr in range(t):
        
        # Lê o valor de 'n'
        n = int(input().strip())
        
        # Chama a função 'findDigits' para encontrar os dígitos divisíveis por 'n'
        resultado = findDigits(n)
        
        # Exibe o resultado encontrado para o caso de teste atual
        print(str(resultado) + '\n')