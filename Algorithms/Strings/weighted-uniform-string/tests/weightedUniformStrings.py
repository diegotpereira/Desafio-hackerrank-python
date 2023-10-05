# A tarefa do problema "Weighted Uniform Strings" no HackerRank é determinar 
# se uma string é "válida" ou "inválida" seguindo certas regras.

# Dada uma string contendo apenas letras minúsculas do alfabeto inglês, 
# a tarefa é verificar se a string é "válida" ou "inválida". A string é 
# considerada "válida" se a soma dos pesos dos seus caracteres for igual 
# a um dos valores que podem ser obtidos a partir de uma sequência de pesos.

# Os pesos dos caracteres são calculados com base na posição do caractere 
# no alfabeto inglês. Por exemplo, o caractere 'a' tem peso 1, o caractere 'b' 
# tem peso 2, e assim por diante até o caractere 'z' com peso 26.

# Além disso, uma substring contígua de uma string é considerada válida se a 
# soma dos pesos dos seus caracteres for igual a um dos valores que podem ser 
# obtidos a partir da sequência de pesos.

# A saída do problema deve ser uma série de respostas "Yes" ou "No", indicando 
# se cada substring da string original é "válida" ou "inválida".

def weightedUniformStrings(string, consultas):
    
    # Criando um conjunto vazio chamado string1 para 
    # armazenar os pesos das substrings uniformes
    string1 = set()
    
    # Inicializando a variável 'atual' com o peso 
    # do primeiro caractere da string
    atual = (ord(string[0]) - 96)
    
    # Adicionando o peso do primeiro caractere ao conjunto string1
    string1.add(atual)
    
    # Iterando sobre a string a partir do segundo caractere
    for i in range(1, len(string)):
        
        # Verificando se o caractere atual é igual ao caractere anterior
        if string[i - 1] == string[i]:
            
            # Se for igual, adiciona o peso do caractere atual 
            # ao peso acumulado (atual)
            atual += (ord(string[i]) - 96)
            
        else:
            
            # Se for diferente, redefine o peso acumulado (atual) 
            # para o peso do caractere atual
            atual = (ord(string[i]) - 96)
            
        # Adicionando o peso acumulado ao conjunto string1
        string1.add(atual)
        
    # Criando uma lista vazia chamada resposta para armazenar 
    # as respostas para as consultas
    resposta = []
    
    # Iterando sobre as consultas
    for i in consultas:
        
        # Verificando se a consulta (i) está presente no conjunto 
        # string1 (ou seja, se existe uma substring uniforme com esse peso)
        if i not in string1:
            
            # Se não estiver presente, adiciona "No" à lista resposta
            resposta.append("No")
            
        else:
            
            # Se estiver presente, adiciona "Yes" à lista resposta
            resposta.append("Yes")
            
    # Retornando a lista resposta contendo as respostas para cada consulta
    return resposta