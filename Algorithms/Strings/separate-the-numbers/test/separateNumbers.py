# A tarefa no link fornecido é chamada "Separate the Numbers" 
# e está hospedada no site HackerRank. É um desafio de programação 
# que envolve a manipulação de sequências de números.

# A descrição completa do problema pode ser encontrada no link 
# que você forneceu. Em resumo, o problema solicita que você 
# verifique se uma determinada sequência de números pode ser 
# dividida em uma série de números crescentes consecutivos. Se 
# for possível fazer essa divisão, você também precisa determinar 
# o primeiro número dessa série.

# Para resolver esse desafio, você precisará escrever um programa 
# ou função que recebe a sequência de números como entrada e retorna 
# a resposta solicitada, conforme as especificações detalhadas no 
# problema.

# Recomenda-se visitar o link e ler atentamente a descrição do 
# problema, juntamente com as instruções sobre o formato da entrada 
# e as restrições. Além disso, você pode encontrar exemplos de 
# entrada e saída para entender melhor o que é esperado como 
# resultado.


def separateNumbers(s):
    
    # Loop para percorrer os possíveis tamanhos de números iniciais
    for i in range(1, len(s) // 2 + 1):
        
        # Verifica se o primeiro caractere da sequência é '0'
        # Se for, pula para a próxima iteração
        if s[0] == '0':
            
            continue
        
        # Obtém o número inicial da sequência
        num = s[:i]
        
        # Inicializa uma sequência válida com o número inicial
        s_valido = num
        
        # Inicializa um contador para o próximo número na sequência
        contador = 1
        
        # Loop para construir a sequência a partir do número inicial
        while len(s_valido) < len(s):
            
            # Calcula o próximo número na sequência
            proximo_num = int(num) + contador
            s_valido += str(proximo_num)
            
            # Incrementa o contador para o próximo número
            contador += 1
            
        # Verifica se a sequência construída é igual 
        # à sequência original
        if s_valido == s:
            
            # Retorna a sequência válida encontrada
            return (f'YES {num}')
        
    # Caso nenhuma sequência válida seja encontrada
    return ('NO')
    
# def separateNumbers(s):
    
#     # Obtém o comprimento da sequência
#     n = len(s)
    
#     # Loop para percorrer os possíveis 
#     # tamanhos de números iniciais
#     for i in range(1,1+n//2):
        
#         # Obtém o número inicial da sequência
#         temp_int = int(s[:i])
        
#         # Inicializa um contador para o 
#         # próximo número na sequência
#         j=0
        
#         # String temporária para construir a sequência
#         temp_str = ""
        
#         # Loop para construir a sequência a partir do número inicial
#         while(len(temp_str) < n):
            
#             # Adiciona o próximo número na sequência à string temporária
#             temp_str += str(temp_int + j)
            
#             # Incrementa o contador para o próximo número
#             j += 1
            
#         # Verifica se a sequência construída é igual à sequência original            
#         if temp_str == s:
#             return("YES {}".format(temp_int))
        
#     # Caso nenhum número seja encontrado
#     return("NO")




# def separateNumbers(s):
    
#     # Variável para armazenar o número encontrado
#     encontrado = 0 
    
#     # Loop para percorrer todos os possíveis tamanhos 
#     # de números iniciais
#     # len(s) retorna o comprimento total da sequência s. 
#     # Por exemplo, se s for "12345", len(s) será igual a 5.

#     # len(s) // 2 divide o comprimento da sequência por 2 
#     # usando a divisão inteira. Isso retorna a metade do 
#     # comprimento da sequência. Por exemplo, se s tiver 
#     # comprimento 5, len(s) // 2 será igual a 2.

#     # Adicionamos 1 ao resultado da divisão inteira para 
#     # garantir que o valor final inclua a metade inteira 
#     # arredondada para cima. Por exemplo, se s tiver 
#     # comprimento 5, (len(s) // 2) + 1 será igual a 3.

#     # O resultado final é passado para a função 
#     # range(1, (len(s) // 2) + 1), que cria um intervalo 
#     # de números de 1 a 2 (inclusive), no exemplo dado.
#     for x in range(1, (len(s) // 2) + 1):
        
#         # Índice para percorrer a sequência
#         indice = x 
        
#         # Lista para armazenar a sequência de números
#         # s[:x] é uma fatia da sequência s que inclui os 
#         # primeiros x caracteres. Por exemplo, se s for 
#         # "12345" e x for 3, s[:x] retornará a string "123".

#         # [s[:x]] cria uma lista com um único elemento, que 
#         # é a substring obtida anteriormente. Neste exemplo, 
#         # a lista value conterá ["123"].
#         value = [s[:x]]
        
#         # Loop para construir a sequência a partir do número inicial
#         while indice < len(s): 
            
#             # Próximo número na sequência
#             # value[-1] retorna o último elemento da lista value. 
#             # Nesse caso, o último elemento é o valor numérico 
#             # anteriormente adicionado à sequência. Por exemplo, 
#             # se value for ['123', '124'], value[-1] retornará '124'.

#             # int(value[-1]) converte o valor numérico em uma 
#             # representação inteira. Isso é necessário para realizar 
#             # operações aritméticas com o número. Por exemplo, se 
#             # value[-1] for '124', int(value[-1]) será igual a 124.

#             # int(value[-1]) + 1 realiza a adição de 1 ao valor 
#             # anterior, obtendo assim o próximo valor na sequência. 
#             # No exemplo dado, o próximo valor será 124 + 1 = 125.

#             # str(int(value[-1]) + 1) converte o resultado de volta 
#             # para uma string. Isso é necessário para garantir que o 
#             # próximo valor seja uma string e possa ser concatenado 
#             # adequadamente à sequência. No exemplo dado, o próximo 
#             # valor será a string '125'.
#             proximo_valor = str(int(value[-1]) + 1)
            
#              # Atualiza o índice para o próximo número na sequência
#             indice += len(proximo_valor)
            
#             # Adiciona o próximo número à sequência
#             value.append(proximo_valor)
        
        
#         # Verifica se a sequência construída é igual 
#         # à sequência original
#         if ''.join(value) == s: 
            
#             # Armazena o número encontrado
#             encontrado = value[0]
            
#     # Retorna o resultado final
#     return('YES {}'.format(encontrado) if encontrado else 'NO')