# No problema "Caesar Cipher 1" do HackerRank, a tarefa é criar um programa que criptografe 
# uma mensagem usando a Cifra de César, um tipo de cifra de substituição na qual cada letra 
# do texto original é substituída por outra letra que está a um número fixo de posições à 
# sua frente no alfabeto.

# Aqui estão os detalhes da tarefa:

# Dada uma string contendo apenas caracteres alfabéticos (maiúsculos e minúsculos) e um valor 
# inteiro k, que representa o número de posições que cada letra deve ser deslocada no alfabeto, 
# a tarefa é criptografar a mensagem substituindo cada letra por outra letra que esteja k posições 
# à frente no alfabeto. Por exemplo, se k for 1, 'a' seria substituído por 'b', 'b' por 'c', e assim 
# por diante. Se k for 3, 'a' seria substituído por 'd', 'b' por 'e', e assim por diante.

# O programa deve preservar a caixa das letras, ou seja, letras maiúsculas devem ser mantidas como 
# maiúsculas e letras minúsculas como minúsculas. Quaisquer outros caracteres não alfabéticos 
# (como espaços, números ou símbolos) não devem ser alterados.

# A tarefa é, portanto, implementar uma função ou método que receba a string original e o valor 
# de k como entrada e retorne a string criptografada de acordo com as regras descritas acima.

# def caesarCipher(string, numeroGiros):
    
#     # Inicializando uma string vazia para armazenar a mensagem criptografada
#     resposta = ""
    
#     # Percorrendo cada caractere na string de entrada
#     for i in range(len(string)):
        
#         # Convertendo o caractere atual para o seu valor ASCII
        
#         # A função ord() em Python é uma função interna que retorna o valor 
#         # inteiro representando o código Unicode de um único caractere. Em 
#         # outras palavras, ela retorna o valor numérico associado a um 
#         # caractere específico de acordo com a tabela Unicode.
#         valorAsci = ord(string[i])
        
#         # Verificando se o caractere é uma letra maiúscula (valores ASCII de 'A' a 'Z')
#         if valorAsci >=  65 and valorAsci <= 90:
            
#             # Criptografando o caractere maiúsculo e adicionando-o à string resultante
#             resposta += chr((valorAsci - 65 + numeroGiros) % 26 + 65)
            
#         # Verificando se o caractere é uma letra minúscula (valores ASCII de 'a' a 'z')
#         elif valorAsci >= 97 and valorAsci <= 122:
            
#             # Criptografando o caractere minúsculo e adicionando-o à string resultante
#             resposta += chr((valorAsci - 97 + numeroGiros) % 26 + 97)
            
#         # Se o caractere não for uma letra, mantém o caractere original
#         else:
            
#             resposta += string[i]
            
#     # Retornando a string criptografada
#     return resposta

def caesarCipher(string, numeroGiros):
    
    # Definindo o alfabeto usado na cifra
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    # Inicializando uma string vazia para armazenar a resposta criptografada
    resposta = ""
    
    # Percorrendo cada caractere na string de entrada
    for i in string:
        
        # Verificando se o caractere está presente no alfabeto minúsculo
        if i in alfabeto:
            
            # Criptografando o caractere minúsculo e adicionando-o à resposta
            resposta += alfabeto[(alfabeto.index(i) + numeroGiros) % 26]
            
        # Verificando se o caractere está presente no alfabeto maiúsculo
        elif i  in alfabeto.upper():
            
            # Criptografando o caractere maiúsculo e adicionando-o à resposta
            resposta += alfabeto.upper()[(alfabeto.upper().index(i) + numeroGiros) % 26]
            
        else:
            
            # Se o caractere não estiver no alfabeto, mantém o caractere original
            resposta += i 
        
    # Retornando a resposta criptografada
    return resposta