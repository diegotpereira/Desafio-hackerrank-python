from bigSorting import bigSorting

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    naoTriados = []
    
    for _ in range(entrada):
        
        naoTriados_item = input()
        naoTriados.append(naoTriados_item)
        
    resultado = bigSorting(naoTriados)
    
    print('\n'.join(resultado))
    print('\n')