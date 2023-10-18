from steadyGene import steadyGene

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    gene = input()
    
    resultado = steadyGene(gene)
    
    print(str(resultado) + '\n')