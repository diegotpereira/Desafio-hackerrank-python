# Esta é a definição da função "kangaroo", que recebe 4 argumentos: 
# x1 - posição inicial do primeiro canguru na reta
# v1 - a distância que o primeiro canguru pula a cada salto
# x2 - posição inicial do segundo canguru na reta
# v2 - a distância que o segundo canguru pula a cada salto


def kangaroo(x1, v1, x2, v2):
    
    # Se o primeiro canguru tiver uma velocidade menor ou igual ao segundo canguru,
    # eles nunca se encontrarão, então retorna "NO".
    if v1 <= v2:
        
        return "NO"
    
    # Loop while para calcular a posição de cada canguru a cada pulo e verificar
    # se eles se encontram a cada iteração.
    while (x1 < x2):
        
        x1 += v1
        x2 += v2
        
        # Se eles se encontrarem, retorna "YES"
        if x1 == x2:
            
            return "YES"
    
     # Se o loop terminar e os cangurus nunca se encontrarem, retorna "NO
    return "NO"

def kangaroo(x1, v1, x2, v2):
    resultado = [i for i in range(10000) if (x1+(v1*i))==(x2+(v2*i))]
    
    if len(resultado) >= 1:
        
        return "YES"
    
    else:
        
        return "NO"


# def kangaroo(x1, v1, x2, v2):
    
#     # Verifica se o segundo canguru começa à frente do primeiro e salta mais longe em cada salto do que o primeiro, 
#     # ou se o segundo canguru começa atrás do primeiro e salta menos em cada salto do que o primeiro.
#     # Se isso acontecer, os cangurus nunca vão se encontrar, então retorna "NO".
#     if (x2 > x1 and v2 >= v1) or (x2 < x1 and v2 <= v1):
        
#         return "NO"
    
#     else:
        
#         if abs(x1 - x2) % abs (v1 - v2) == 0:
            
#             return "YES"
#         # Caso contrário, faz outro cálculo para ver se os cangurus vão se encontrar em algum ponto no futuro,
#         # e retorna "YES" se for possível ou "NO" se não for possível.
#         else:
            
#             return "NO"
        
if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    x1 = int(primeira_multipla_entrada[0])
    
    v1 = int(primeira_multipla_entrada[1])
    
    x2 = int(primeira_multipla_entrada[2])

    v2 = int(primeira_multipla_entrada[3])
    
    resultado = kangaroo(x1, v1, x2, v2)
    
    print(resultado + '\n')