from luckBalance import luckBalance

if __name__ == '__main__':
    
    primeira_entrada_multipla = input().rstrip().split()
    
    n = int(primeira_entrada_multipla[0])
    k = int(primeira_entrada_multipla[1])
    
    concursos = []
    
    for _ in range(n):
        
        concursos.append(list(map(int, input().rstrip().split())))
        
    resultado = luckBalance(k, concursos)
    
    print(str(resultado) + '\n')