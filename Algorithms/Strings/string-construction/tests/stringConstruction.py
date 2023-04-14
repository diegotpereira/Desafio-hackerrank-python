

from collections import Counter

def stringConstruction(s):
    
    # cria um objeto Counter a partir da string s
    dic = Counter(s)
    
    # retorna o número de caracteres únicos em s
    return len(dic)

# def stringConstruction(s):
    
#     # cria uma lista de 26 elementos com valor False
#     h = [False] * 26
    
#     # para cada caracter na string s, atualiza o valor correspondente na lista h para True
#     for x in s: h[ord(x) - 97] = True 
    
#     # retorna a quantidade de valores True na lista h
#     return h.count(True)



# def stringConstruction(s):
    
#     """
#     Retorna o número de caracteres únicos em uma string s.
#     """
#     # Cria um conjunto com todos os caracteres únicos na string 's'
#     seen = set(s)
    
#     #  retorna o tamanho do conjunto 
#     return len(seen)


if __name__ == "__main__":
    
    q = int(input().rstrip().split()[0])
    
    for i in range(q):
        
        s = input()
        
        resultado = stringConstruction(s)
        
        print(str(resultado) + "\n")