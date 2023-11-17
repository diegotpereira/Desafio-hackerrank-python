
# Importa a função flippingBits do módulo flippingBits

from flippingBits import flippingBits

# Verifica se o script está sendo executado como um programa principal
if __name__ == '__main__':
    
    # Solicita ao usuário que insira um valor inteiro e remove espaços 
    # em branco desnecessários
    entrada = int(input().strip())
    
    # Loop que itera através do número de casos de teste 
    # especificados por 'entrada'
    for qItr in range(entrada):
        
        # Solicita ao usuário que insira um número inteiro 
        # e remove espaços em branco desnecessários
        n = int(input().strip())
        
        # Chama a função flippingBits com o valor 
        # de 'n' e armazena o resultado
        resultado = flippingBits(n)
        
        # Imprime o resultado seguido por uma nova linha
        print(str(resultado) + '\n')