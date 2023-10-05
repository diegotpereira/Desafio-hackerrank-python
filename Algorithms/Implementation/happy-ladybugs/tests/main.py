from happyLadybugs import happyLadybugs

if __name__ == '__main__':
    
    g = int(input().strip())
    
    for g_itr in range(g):
        
        n = int(input().strip())
        
        b = input()
        
        resultado = happyLadybugs(b)
        
        print(resultado + '\n')