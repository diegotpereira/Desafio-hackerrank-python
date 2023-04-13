# def catAndMouse(x, y, z):
    
#     # Calcula a distância do gato A até o rato
#     distancia_gato_a = abs(x - z)
    
#     # Calcula a distância do gato B até o rato
#     distancia_gato_b = abs(y - z)
    
#     # Se a distância do gato A até o rato for menor que a distância do gato B, retorna "CAT A"
#     if distancia_gato_a < distancia_gato_b:
        
        
#         return "Cat A"
    
#     # Se a distância do gato B até o rato for menor que a distância do gato A, retorna "CAT B"
#     elif distancia_gato_b < distancia_gato_a:
        
#         return "Cat B"
    
#     else:
        
#         # Se ambas as distâncias forem iguais, retorna "Mouse C"
#         return "Mouse C"
    
def catAndMouse(x, y, z):
    
    # Verifica se o rato está exatamente entre os dois gatos
    if abs((x + y) / 2 == z):
        
        return "Mouse C"
    
    # Verifica qual gato está mais próximo do rato e retorna sua letra correspondente
    return "Cat A" if abs(x - z) < abs(y - z) else "Cat B"
    
    

if __name__ == "__main__":
    
    q = int(input())

    for q_itr in range(q):
        
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        resultado = catAndMouse(x, y, z)

        print(resultado + '\n')