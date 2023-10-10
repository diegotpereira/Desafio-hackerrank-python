# No problema "Strings XOR" do HackerRank, você é dado um conjunto de strings e precisa executar operações XOR entre pares de strings. A tarefa é calcular a operação XOR (ou exclusivo) bit a bit entre todas as possíveis combinações de duas strings e encontrar a string que resulta no maior valor após a operação XOR.

# Em resumo, a tarefa envolve os seguintes passos:

# Dado um conjunto de strings, você deve calcular o resultado da operação XOR bit a bit entre todas as possíveis combinações de duas strings no conjunto.

# Encontrar a string que resulta no maior valor após a operação XOR.

# Retornar essa string como resultado.

# A ideia é realizar a operação XOR entre todas as combinações possíveis de duas strings e determinar qual combinação produz o maior valor. A string resultante dessa combinação é a resposta.

# Definindo a função 'strings_xor' com dois parâmetros, 's' e 't'.
def strings_xor(s, t):
    # Inicializa uma string 'res' para armazenar o resultado da operação XOR de cada par de caracteres correspondentes.
    res = ""
    
    # Loop para iterar pelos índices de caracteres em 's'.
    for i in range(len(s)):
        # Verifica se o caractere em 's' na posição 'i' é igual ao caractere correspondente em 't'.
        if s[i] == t[i]: # alteração aqui
            # Se os caracteres forem iguais, acrescente '0' ao resultado 'res'.
            res += '0' # alteração aqui
        else:
            # Se os caracteres forem diferentes, acrescente '1' ao resultado 'res'.
            res += '1' # alteração aqui
    
    # Retorna a string resultante após a operação XOR.
    return res

# Solicita entrada do usuário para as strings 's' e 't'.
s = input("Digite a primeira string (s): ")
t = input("Digite a segunda string (t): ")

# Chama a função 'strings_xor' com as entradas fornecidas e imprime o resultado.
print(strings_xor(s, t))
