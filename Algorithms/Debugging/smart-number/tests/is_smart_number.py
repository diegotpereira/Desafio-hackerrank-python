# Importando o módulo 'math' para utilizar funções matemáticas.
import math

# Definindo uma função chamada 'is_smart_number' que verifica se um número é um "Smart Number".
def is_smart_number(num):
    # Calcula a raiz quadrada inteira do número.
    val = int(math.sqrt(num))
    # Verifica se a divisão do número pelo valor da raiz quadrada é igual ao valor da raiz quadrada.
    if num / val == val: # alteração
        # Se a condição for verdadeira, retorna True (é um "Smart Number").
        return True
    # Caso contrário, retorna False (não é um "Smart Number").
    return False