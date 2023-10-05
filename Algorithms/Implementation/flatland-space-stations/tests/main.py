from flatlandSpaceStations import flatlandSpaceStations

if __name__ == '__main__':
    
    primeira_multipla_Entrada = input().split()
    numero_total_cidades = int(primeira_multipla_Entrada[0])
    m = int(primeira_multipla_Entrada[1])
    
    lista_cidades_com_estacoes = list(map(int, input().rstrip().split()))
    
    #  n (número total de cidades) e c (lista de cidades com estações)
    resultado = flatlandSpaceStations(numero_total_cidades, lista_cidades_com_estacoes)
    
    print(str(resultado) + '\n')
    
    