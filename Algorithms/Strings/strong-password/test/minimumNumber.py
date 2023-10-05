

# A tarefa do problema "Strong Password" no HackerRank é verificar se uma senha é forte ou não, com base em certas regras específicas.

# O problema define que uma senha é forte se atender a essas condições:

# Possuir pelo menos 6 caracteres e no máximo 100 caracteres.
# Deve conter pelo menos um caractere maiúsculo (A-Z).
# Deve conter pelo menos um caractere minúsculo (a-z).
# Deve conter pelo menos um dígito (0-9).
# Deve conter pelo menos um caractere especial do conjunto: "!@#$%^&*()-+"
# A tarefa é implementar uma função chamada minimumNumber(n, password), onde n é o número de caracteres na senha e password é a própria 
# senha fornecida. A função deve calcular o número mínimo de caracteres que precisam ser adicionados à senha para que ela se torne forte, 
# seguindo as regras acima.

# O link fornecido leva à página do HackerRank, onde você pode encontrar o enunciado completo do problema, exemplos de entrada e saída esperada, 
# e também pode realizar a implementação da função em Python para resolver o desafio.

# import re  # Importa o módulo 're' (expressões regulares) para trabalhar com padrões em strings.

# def minimumNumber(n, senha):  # Definição da função minimumNumber que recebe o tamanho da senha 'n' e a senha 'senha' como entrada.

#     contador = 0  # Inicializa o contador com zero para contar o número mínimo de caracteres que precisam ser adicionados à senha.

#     padrao_maiusculo = re.compile('[a-z]')  # Cria um padrão de busca com a expressão regular '[a-z]' para verificar a presença de letras minúsculas na senha.
#     padrao_minusculo = re.compile('[A-Z]')  # Cria um padrão de busca com a expressão regular '[A-Z]' para verificar a presença de letras maiúsculas na senha.
#     padrao_num = re.compile('[0-9]')  # Cria um padrão de busca com a expressão regular '[0-9]' para verificar a presença de dígitos na senha.
#     padrao_caracter_especial =  re.compile('[!@#$%^&*()\-+]')  # Cria um padrão de busca com a expressão regular '[!@#$%^&*()\-+]' para verificar a presença de caracteres especiais na senha.

#     if not bool(re.search(padrao_maiusculo, senha)):  # Verifica se o padrão de letras minúsculas não é encontrado na senha.
#         contador += 1  # Se o padrão de letras minúsculas não for encontrado, incrementa o contador em 1.

#     if not bool(re.search(padrao_minusculo, senha)):  # Verifica se o padrão de letras maiúsculas não é encontrado na senha.
#         contador += 1  # Se o padrão de letras maiúsculas não for encontrado, incrementa o contador em 1.

#     if not bool(re.search(padrao_num, senha)):  # Verifica se o padrão de dígitos não é encontrado na senha.
#         contador += 1  # Se o padrão de dígitos não for encontrado, incrementa o contador em 1.

#     if not bool(re.search(padrao_caracter_especial, senha)):  # Verifica se o padrão de caracteres especiais não é encontrado na senha.
#         contador += 1  # Se o padrão de caracteres especiais não for encontrado, incrementa o contador em 1.

#     if contador + len(senha) >= 6:  # Verifica se o tamanho da senha somado ao contador é maior ou igual a 6 (tamanho mínimo de senha).
#         return contador  # Se o tamanho da senha atender aos requisitos, retorna o valor atual do contador.

#     else:
#         # Se o tamanho da senha não atender aos requisitos, retorna o valor do contador somado à diferença entre 6 e o tamanho atual da senha.
#         # Isso é feito para determinar o número mínimo de caracteres que precisam ser adicionados à senha para que ela se torne forte.
#         return contador + (6 - contador - len(senha))


import re  # Importa o módulo 're' (expressões regulares) para trabalhar com padrões em strings.

def minimumNumber(n, senha):  # Definição da função minimumNumber que recebe o tamanho da senha 'n' e a senha 'senha' como entrada.

    # A função max() é usada para retornar o maior valor entre o resultado de 6 - n e a soma de uma série de valores 0 ou 1.
    # Essa série de valores é baseada na verificação da presença de caracteres especiais, dígitos, letras maiúsculas e minúsculas na senha.

    return max(6 - n,  # Retorna a maior entre a diferença entre 6 e o tamanho da senha e o resultado da soma a seguir.

        # A soma a seguir consiste em 0 se o padrão for encontrado na senha, caso contrário, é 1.
        # Ou seja, cada expressão re.search() verifica se o padrão (dígitos, letras maiúsculas, letras minúsculas e caracteres especiais)
        # está presente na senha. Se o padrão estiver presente, a expressão re.search() retorna um objeto correspondente (verdadeiro),
        # e a expressão é avaliada como 0. Se o padrão não estiver presente, a expressão re.search() retorna None (falso),
        # e a expressão é avaliada como 1.

        sum((
            0 if re.search('[0-9]', senha) else 1,  # Verifica a presença de dígitos na senha.
            0 if re.search('[a-z]', senha) else 1,  # Verifica a presença de letras minúsculas na senha.
            0 if re.search('[A-Z]', senha) else 1,  # Verifica a presença de letras maiúsculas na senha.
            0 if re.search('[@!#$%^&*()+-]', senha) else 1,  # Verifica a presença de caracteres especiais na senha.
        ))
    )
