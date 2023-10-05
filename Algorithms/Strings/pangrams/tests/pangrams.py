# A tarefa do problema "Pangrams" no HackerRank é 
# determinar se uma dada string é um "pangrama". 
# Um pangrama é uma frase que contém todas as letras 
# do alfabeto pelo menos uma vez.

# Na descrição do problema, é fornecida uma string de 
# entrada que pode conter letras maiúsculas, minúsculas, 
# números, pontuações e espaços. A tarefa é escrever uma 
# função ou programa que determine se essa string é um pangrama ou não.

# Para resolver o problema, você precisa percorrer a 
# string de entrada, ignorar caracteres que não são letras 
# e manter um conjunto de letras que já apareceram na 
# string. Em seguida, verifique se o conjunto contém todas 
# as letras do alfabeto. Se todas as letras do alfabeto 
# estiverem presentes, a string é um pangrama, e a função 
# ou programa deve retornar "pangrama". Caso contrário, 
# deve retornar "não pangrama".

# def pangrams(string):
    
#     # Criando um conjunto vazio para armazenar 
#     # as letras presentes na string
#     letras_presentes =  set()
    
#     # Percorrendo cada caractere da string de entrada
#     for caracter in string:
        
#         # Verificando se o caractere é uma letra do alfabeto
#         # isalpha() é uma função nativa em Python. É um método 
#         # embutido (built-in) da classe str (string) que retorna 
#         # True se todos os caracteres da string são letras do 
#         # alfabeto (alfabéticos) e False caso contrário.
#         if caracter.isalpha():
            
#             # Adicionando a letra (convertida para minúscula) 
#             # ao conjunto de letras_presentes
#             letras_presentes.add(caracter.lower())
            
#     # Criando um conjunto com todas as letras do alfabeto
#     alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    
#     # Verificando se o conjunto de letras_presentes contém 
#     # todas as letras do alfabeto
#     if letras_presentes >= alfabeto:
        
#         # Se todas as letras do alfabeto estiverem presentes, 
#         # retorna 'pangram'
#         return 'pangram'
    
#     else:
        
#         # Caso contrário, retorna 'not pangram'
#         return 'not pangram'
    
# def pangrams(string):
    
#     # Definindo a string contendo todas as letras do alfabeto
#     alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
#     # Convertendo a string de entrada em letras minúsculas, 
#     # removendo duplicatas e convertendo em uma lista
#     lista = list(set(string.lower()))
    
#     # Ordenando a lista em ordem alfabética
#     lista.sort()
    
#     # Verificando se há um espaço (' ') na lista e, 
#     # se houver, removendo-o
#     if ' ' in lista:
        
#         # Unindo os caracteres da lista em uma nova string
#         lista.remove(' ')
        
#     # Unindo os caracteres da lista em uma nova string
#     nova_string = ''.join(lista)
    
#     # Verificando se a nova string é igual à string que contém 
#     # todas as letras do alfabeto
#     if nova_string == alfabeto:
        
#         # Se a nova string for igual ao alfabeto, retorna 'pangram'
#         return 'pangram'
    
#     else:
        
#         # Caso contrário, retorna 'not pangram'
#         return 'not pangram'

# def pangrams(string):
    
#     # Criando um conjunto a partir da string convertida em letras minúsculas
#     # O conjunto removerá automaticamente caracteres duplicados
#     conjunto_letras = set(string.lower())
    
#     # Verificando se o tamanho do conjunto é igual a 27
#     # Se o conjunto contiver todas as 26 letras do alfabeto (sem duplicatas) e um espaço em branco (' '), terá tamanho 27
#     # Caso contrário, terá um tamanho menor que 27
#     # Portanto, se o conjunto tiver tamanho 27, a string é um pangrama, caso contrário, não é
#     return 'pangram' if len(conjunto_letras) == 27 else 'not pangram'

# import string

# def pangrams(s):
    
#     # Armazenando a string contendo todas as letras minúsculas do alfabeto
#     palavra = string.ascii_lowercase
    
#     # Percorrendo cada letra da string 'palavra' (todas as letras minúsculas do alfabeto)
#     for i in palavra:
        
#         # Verificando se a letra 'i' não está presente na string 's' (convertida para letras minúsculas)
#         if i not in s.lower():
            
#             # Se alguma letra não estiver presente em 's', a string não é um pangrama
#             return 'not pangram'
        
#     # Se todas as letras do alfabeto estiverem presentes em 's', a string é um pangrama
#     return 'pangram'


# def pangrams(s):
    
#     # Criando um conjunto (palavra) contendo todas as letras minúsculas do alfabeto
#     # Utiliza a função range para criar um intervalo de valores entre as ordens das letras 'a' e 'z'
#     # Em seguida, utiliza list comprehension para converter cada valor em seu caractere correspondente
#     # Por fim, transforma a lista em um conjunto para remover duplicatas
#     palavra = set([chr(c) for c in range(ord('a'), ord('z'))])
    
#     # Verificando se a diferença entre o conjunto palavra e o conjunto das letras minúsculas da string 's' é vazio
#     # Se a diferença for vazia, isso significa que todas as letras do alfabeto estão presentes na string
#     # Portanto, é um pangrama
#     # Caso contrário, se houver alguma letra que não esteja presente, não é um pangrama
#     return 'pangram' if len(palavra.difference(s.lower())) == 0 else 'not pangram'



def pangrams(s):
    
    # Convertendo a string para letras minúsculas 
    # para garantir a contagem correta das letras
    s = s.lower()
    
    # Convertendo a string em um conjunto para 
    # remover duplicatas e contar as letras únicas
    s = set(s)
    
    # Criando um conjunto contendo todas as letras 
    # minúsculas do alfabeto ('a' a 'z')
    abc = set(map(chr, range(97, 123)))
    
    # Verificando se o conjunto das letras minúsculas 
    # do alfabeto está contido no conjunto 's'
    # Ou seja, se todas as letras do alfabeto estão 
    # presentes na string 's'
    if abc & s == abc:
        
        # Se todas as letras do alfabeto estiverem 
        # presentes, retorna 'pangram'
        return 'pangram'
    
    else:
        
        # Caso contrário, retorna 'not pangram'
        return 'not pangram'