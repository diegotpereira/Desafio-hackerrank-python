# O problema "Beautiful Days at the Movies" pede para contar quantos dias "bonitos" 
# (ou seja, dias em que a diferença entre o número original e seu reverso é divisível por k) 
# existem entre dois números i e j (inclusive).

# A lógica do problema é converter cada número em uma string e, em seguida, reverter a ordem 
# dos caracteres dessa string para obter o número reverso. Em seguida, a diferença entre o número 
# original e seu reverso é calculada e verificada se é divisível por k. Se a diferença for divisível 
# por k, o dia é considerado "bonito" e o contador é incrementado. No final, a função retorna o número 
# total de dias "bonitos".

# def beautifulDays(i, j, k):
    
#     # inicializa a variável "contar" com zero
#     contar = 0
        
#     # percorre todos os números entre "i" e "j"
#     for num in range(i, j + 1):
        
#         # converte o número em string e armazena na variável "reverter_string"
#         reverter_string = str(num)
        
#          # verifica se a diferença entre o número original e seu reverso é divisível por "k"
#         if abs(num - int(reverter_string[::-1])) % k == 0:
            
#             # se a condição acima for satisfeita, incrementa a variável "contar" em 1
#             contar += 1
        
#     # retorna o valor final da variável "contar"
#     return contar

"""
Explicação:
    1 - Eu uso a função *map()* para aplicar a função *lambda* a todos os elementos no intervalo de i a j.
    2 - A função lambda retorna True se um lembrete de divisão do elemento do intervalo e sua versão reversa for igual a 0.
    3 - O próximo passo é usar a função *list()* no objeto de mapa retornado para convertê-lo em lista
    4 - Em seguida apliquei a função *sum()* na lista para contar quantos belos dias tem o range, ou seja, somamos todos os valores True na lista, por exemplo apliquei a função *sum()* na lista[False, True, False] produziria o valor 1
"""

def beautifulDays(i, j, k):
    
    # Cria uma lista com números de i a j e verifica se cada número é "bonito"
    # (ou seja, sua diferença para o número invertido é divisível por k).
    # Em seguida, soma os resultados True para obter o número de dias bonitos.
    
    return sum(list(map(lambda x : abs(x - int(str(x)[::-1])) % k == 0, range(i, j + 1))))


# def diferenca(x, k):
    
#     # retorna 1 se a diferença entre x e o seu reverso é divisível por k, caso contrário retorna 0
#     return 1 if abs(x - int(str(x)[::-1])) % k == 0 else 0
    
# def beautifulDays(i, j, k):
    
#     # retorna a soma das diferenças "bonitas" entre i e j
#     return sum(diferenca(x, k) for x in range(i, j + 1))
    

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    i = int(primeira_multipla_entrada[0])
    
    j = int(primeira_multipla_entrada[1])
    
    k = int(primeira_multipla_entrada[2])
    
    resultado = beautifulDays(i, j, k)
    
    # print(resultado + '\n')
    print(str(resultado) + '\n')