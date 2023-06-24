def funnyString(s):
    
    # Lista para armazenar as diferenças 
    # absolutas dos caracteres adjacentes
    l = []
    
     # Percorre a string até o penúltimo caractere
    for i in range(len(s) - 1):
        
        l.append(abs(ord(s[i]) - ord(s[i + 1])))
        
    if l == l[::-1]:
        
        return "Funny"
    
    return "Not Funny"