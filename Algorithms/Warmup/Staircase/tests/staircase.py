

# def staircase(n):
    
#     # Verifica se n é negativo e lança uma exceção em caso afirmativo
#     if n < 0:
        
#         raise ValueError("n deve ser não negativo")
    
#     # Define a string "s" como um espaço em branco e a string "x" como uma cerquilha (#)
#     s = " "
#     x = "#"
    
#     # Inicializa uma lista vazia que será usada para armazenar as linhas da escada
#     linhas = []
    
#     # Percorre um loop de 0 a n - 1 (inclusive)
#     for i in range(n):
        
#         # Cria uma nova linha da escada, com "n - (i + 1)" espaços em branco seguidos de "(i + 1)" cerquilha(s)
#         linha = s * (n - (i + 1)) + x * (i + 1)
        
#         # Adiciona a nova linha à lista de linhas
#         linhas.append(linha)
        
#     # Retorna a lista de linhas como uma única string, com cada linha separada por uma quebra de linha
#     return "\n".join(linhas)

# def staircase(n):
    
#     if n < 0:
#         raise ValueError("n deve ser não negativo")
    
#     linha = ""
    
#     for i in range(1, n):
        
#         return (" " * (n - i) + "#" * i)
    
#     return ("#" * n)

def staircase(n):
    
    space = ' '
    hashtag = '#'
    for i in range(n):
        j = n-1-i
        k = i+1
        return(space*j + hashtag*k)
    


if __name__ == "__main__":

    n = int(input().strip())
    
    staircase(n)

    resultado = staircase(n)

    print(resultado)