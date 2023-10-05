# No problema "Mars Exploration" do HackerRank, a tarefa é simular 
# a comunicação entre sondas espaciais e a Terra. O problema é 
# inspirado na suposição de que as comunicações entre a Terra e 
# uma sonda espacial enviada a Marte podem ser corrompidas durante 
# a transmissão.

# A mensagem enviada pela sonda espacial consiste em uma sequência 
# de letras "S", "O" e "S". No entanto, devido às más condições de 
# transmissão, algumas letras podem ser alteradas durante o processo 
# de envio e recebimento.

# A mensagem original da sonda é sempre uma sequência repetitiva de 
# "SOS", que é o código padrão para uma comunicação de sucesso. No 
# entanto, algumas letras "S" ou "O" podem ser corrompidas, 
# resultando em mensagens como "SOO", "SSS", "OSS" e assim por diante.

# A tarefa do problema é determinar quantas letras da mensagem 
# foram corrompidas durante a transmissão, com base na mensagem recebida 
# pela Terra. Dado o comprimento da mensagem recebida, você precisa 
# contar quantas letras estão fora do padrão "SOS".

# Por exemplo, se a mensagem recebida for "SOSSPSSQSSOR", você 
# deve determinar que duas letras foram corrompidas e que a 
# mensagem original da sonda era "SOSSOSSOSSOS".

# Para resolver o problema, você pode implementar uma função ou 
# método que receba a string da mensagem recebida como entrada, 
# verifique cada conjunto de três letras e conte quantas letras foram corrompidas.

# def marsExploration(string):
    
#     # Obtendo o tamanho da mensagem (quantidade total de caracteres)
#     tamanho_mensagem = len(string)

#     # Inicializando o contador de letras corrompidas
#     letras_corrompidas = 0
    
#     # Percorrendo a mensagem de 3 em 3 caracteres, começando do índice 0
#     for i in range(0, tamanho_mensagem, 3):
        
#         # Obtendo o conjunto atual de 3 caracteres
#         conjunto_atual = string[i:i + 3]
        
#         # Verificando se o conjunto atual é diferente de "SOS" (não está intacto)
#         if conjunto_atual !=  "SOS" :
            
#             # Se o conjunto não for igual a "SOS", percorremos cada caractere
#             for j in range(3):
                
#                 # Verificando caractere por caractere se é diferente do conjunto "SOS" correspondente
#                 if conjunto_atual[j] != "SOS"[j]:
                    
#                     # Se encontrarmos uma letra diferente, incrementamos o contador de letras corrompidas
#                     letras_corrompidas += 1
                    
#     # Retornando o total de letras corrompidas na mensagem
#     return letras_corrompidas
    
    
# def marsExploration(string):
    
#     # Retornar a soma de uma lista criada através de compreensão de lista
#     # que verifica se cada caractere da string é diferente do caractere correspondente em "SOS" usando i % 3.
#     # Se for diferente, adiciona 1 à lista; caso contrário, adiciona 0.
#     return sum([1 if string[i] != "SOS"[i % 3] else 0 for i in range(len(string))])

# def marsExploration(string):
#     # Obter o tamanho da string
#     tamanhoString = len(string)
#     contador = 0

#     # Percorrer cada caractere da string
#     for i in range(tamanhoString):
        
#         # Verificar o índice para identificar os caracteres esperados
#         if i % 3 == 0:
            
#             # Verificar se o caractere não é 'S' (a primeira letra de "SOS")
#             if string[i] != 'S':
#                 contador += 1  # Incrementar o contador se a letra estiver corrompida

#         elif i % 3 == 1:
            
#             # Verificar se o caractere não é 'O' (a segunda letra de "SOS")
#             if string[i] != 'O':
#                 contador += 1  # Incrementar o contador se a letra estiver corrompida

#         else:  # i % 3 == 2
            
#             # Verificar se o caractere não é 'S' (a terceira letra de "SOS")
#             if string[i] != 'S':
#                 contador += 1  # Incrementar o contador se a letra estiver corrompida

#     return contador  # Retornar o total de letras corrompidas


def marsExploration(string):
    
    # Definindo a sequência original de comparação
    original = "SOS"
    
    # Inicializando a variável para contar as alterações
    alterado = 0
    
    # Iterando sobre cada letra da string de entrada
    for letra in range(len(string)):
        
        # Comparando a letra da string de entrada com a letra correspondente na sequência original
        # Se forem diferentes, significa que houve uma alteração e incrementamos a variável 'alterado'
        alterado += string[letra] !=  original[letra % 3]
        
    # Retornando o número total de alterações
    return alterado