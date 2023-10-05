from weightedUniformStrings import weightedUniformStrings

if __name__ == '__main__':
    
    string = input()
    
    quantidade_consultas = int(input().strip())
    
    consultas = []
    
    for _ in range(quantidade_consultas):
        
        consultas_item = int(input().strip())
        consultas.append(consultas_item)
        
        resultado = weightedUniformStrings(string, consultas)
        
        print('\n'.join(resultado))
