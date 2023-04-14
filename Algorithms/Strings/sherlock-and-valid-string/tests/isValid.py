
from collections import Counter

def isValid(s):
    
    contar = list(Counter(s).values())
    
    frequencias = set(contar)
    
    if len(frequencias) == 1:
        
        return "YES"
    
    if len(frequencias) > 2:
        
        return "NO"
    
    um_tempo_frequencia = contar.count(1)
    
    if um_tempo_frequencia == 1:
        
        return "YES"
    
    if um_tempo_frequencia > 1:
        
        return "NO"
    
    lista_set = list(frequencias)
    
    if abs(lista_set[0] - lista_set[1] == 1):
        
        return "YES"
    
    return "NO"

if __name__ == "__main__":
    
    s = input()
    
    resultado = isValid(s)
    
    print(resultado + '\n')