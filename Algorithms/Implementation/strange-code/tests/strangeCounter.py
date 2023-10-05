# Um contador estranho exibe um valor 
# que diminui em uma sequência 
# incomum. Ele começa em um valor 
# específico e diminui a cada ciclo 
# de tempo. No primeiro ciclo, ele 
# diminui do valor inicial para a
# metade do valor inicial, 
# arredondando para baixo. No 
# segundo ciclo, ele diminui do 
# valor da metade do valor inicial 
# para um quarto do valor inicial, 
# novamente arredondando para baixo. 
# O padrão continua, diminuindo pela 
# metade do valor anterior em cada ciclo.

# Sua tarefa é determinar qual valor 
# é exibido no contador estranho em um 
# determinado instante de tempo.

# A entrada do problema consiste em 
# um único número inteiro, o tempo 
# no qual você precisa determinar o 
# valor exibido no contador estranho. 
# Você deve calcular e retornar esse 
# valor com base nas regras descritas.


# # Importa o módulo math, que fornece funções matemáticas
# import math

# # Função que calcula o valor exibido no contador estranho.
# def strangeCounter(entrada):
    
#     # Calcula o número de ciclos baseado no tempo de entrada.
#     ciclo_entrada = math.ceil(math.log2(entrada / 3 + 1))
    
#     # Calcula o valor exibido no início do ciclo ciclo_entrada
#     inicio_ciclo = 2 ** ciclo_entrada * 3
    
#     # Calcula o valor atual exibido no contador estranho e retorna.
#     return inicio_ciclo - entrada - 2


# # Função que calcula o valor exibido no contador estranho

# def strangeCounter(entrada):
    
#     # Variável contador representa o valor exibido no contador
#     contador = 3
    
#     # Variável j controla o aumento do valor exibido a cada ciclo
#     ciclo = 3
    
#     # Executa o loop enquanto o valor exibido for menor do que o tempo de entrada
#     while contador < entrada:
        
#         # Atualiza o valor exibido para o próximo ciclo
#         contador = contador + 2 * ciclo
        
#         # Dobra o aumento para o próximo ciclo
#         ciclo = 2 * ciclo 
        
#     # Calcula e retorna o valor atual exibido no contador estranho
#     return contador - entrada + 1

# Função que calcula o valor exibido no contador estranho

# def strangeCounter(entrada):
    
#     # Inicializa o valor exibido no contador
#     valor = 3 
    
#     # Loop infinito para calcular o valor
#     while True:
        
#         # Calcula o tempo inicial do ciclo atual
#         tempo1 = valor - 2
        
#         # Calcula o tempo final do ciclo atual
#         tempo2 = (valor * 2) - 2
        
#         # Verifica se o tempo de entrada está dentro do ciclo atual
#         if (entrada < tempo2):
            
#             # Se o tempo de entrada estiver entre o valor exibido e o tempo2:
#             if entrada >= valor: 
                
#                 # Calcula a diferença de tempo entre entrada e valor exibido
#                 contador = entrada - valor
                
#                 # Calcula o novo valor exibido no contador
#                 novo_valor = tempo1 - contador
                
#                 # Retorna o novo valor exibido
#                 return novo_valor
            
#             # Se o tempo de entrada for menor do que o valor exibido:
#             else:
                
#                 # Calcula a diferença de tempo entre valor exibido e entrada
#                 contador = valor - entrada
                
#                 # Calcula o novo valor exibido no contador
#                 novo_valor = entrada + contador
                
#                 # Retorna o novo valor exibido
#                 return novo_valor
        
#         # Se o tempo de entrada não estiver dentro do ciclo atual:
#         else:
            
#             # Dobra o valor exibido para o próximo ciclo
#             valor *= 2


# Função que calcula o valor exibido no contador estranho

def strangeCounter(entrada):
    
    # Variável para acompanhar o tamanho acumulado do ciclo
    tamanho = 0
    
    # Variável i que controla o incremento do tamanho do ciclo
    i = 3
    
    # Loop enquanto o tamanho acumulado for menor do que o tempo de entrada
    while tamanho < entrada:
        
        # Incrementa o tamanho acumulado do ciclo
        tamanho += i
        
        # Dobra o valor de i para o próximo ciclo
        i = i * 2
        
    # Calcula e retorna o valor exibido no contador estranho no tempo de entrada
    return tamanho + 1 - entrada