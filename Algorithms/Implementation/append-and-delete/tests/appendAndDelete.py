# s -> A primeira linha contém uma string, a string inicial.
# t -> A segunda linha contém uma string, a string final desejada.
# k -> A terceira linha contém um inteiro, o número de operações

# Esse código implementa a função appendAndDelete(s, t, k), que recebe 
# duas strings s e t e um inteiro k. A função retorna "YES" se for 
# possível transformar a string s na string t em k ou menos operações, 
# caso contrário retorna "NO".

# def appendAndDelete(s, t, k):
    
#     # Verifica se a diferença entre o tamanho de s e t é maior do que k
#     if abs(len(s) - len(t)) > k :
        
#         # Se for, não é possível transformar s em t em k operações ou menos
#         return "NO"
    
#     i = 0
    
#     # Enquanto houver caracteres iguais em s e t, incrementa o índice i
#     while i < len(s) and len(t) and s[i] == t[i]:
        
#         i += 1
        
#     # Calcula o número de operações necessárias para transformar s em t
#     num_operacoes = len(s) - i
    
#     num_operacoes += len(t) - i
    
#     # Verifica se o número de operações é menor ou igual a k
#     if num_operacoes <= k:
        
#         return "YES"

#     return "NO"

def appendAndDelete(primeira_string, nova_string, numero_operacoes):
    
    # Verifica se as strings são iguais
    if primeira_string == nova_string:
        
        return "YES"
    
    # Calcula a diferença de tamanho entre as strings
    diferenca = abs(len(primeira_string) - len(nova_string))
    
    # Verifica se a diferença é maior que o número máximo de operações permitido
    if diferenca > numero_operacoes:
        
        return "NO"
    
    # Inicia a contagem de operações
    contar = numero_operacoes 
    
    # Percorre as strings caractere por caractere até encontrar um caractere diferente
    for i in range(min(len(primeira_string), len(nova_string))):
        
        # Verifica se o caractere atual é diferente nas duas strings e se há operações restantes para serem realizadas
        if primeira_string[i] != nova_string[i] and contar >= diferenca:
            
            contar -= 1
            
        else:
            
            break
        
    # Verifica se ainda há operações restantes ou se o número de operações não é suficiente para transformar uma string na outra
    if contar < diferenca or (contar - diferenca) % 2 != 0:
        
        return "NO"
    
    else:
        
        return 'YES'
    
    

if __name__ == "__main__":
    
    s = input()

    t = input()

    k = int(input().strip())

    resultado = appendAndDelete(s, t, k)

    print(resultado + '\n')