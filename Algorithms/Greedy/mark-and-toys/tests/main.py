from maximumToys import maximumToys

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    n = int(primeira_multipla_entrada[0])
    orcamento = int(primeira_multipla_entrada[1])
    precos = list(map(int, input().rstrip().split()))
    
    resultado = maximumToys(precos, orcamento)
    
    print(str(resultado) + '\n')