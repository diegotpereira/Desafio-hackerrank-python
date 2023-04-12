
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     contar_macas = [(i + a) for i in apples if s <= (i + a) <= t]
#     contar_laranjas = [(j + b) for j in oranges if s <= (j + b) <= t]
    
#     print(len(contar_macas), len(contar_laranjas), sep = "\n")

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    macas = [a + x for x in apples]
    laranjas = [b + x for x in oranges]
    
    a_contar = 0
    b_contar = 0
    
    for i in apples:
        
        if s <= i <= t:
            
            a_contar += 1
            
    for j in oranges:
        
        if s <= j <= t:
            
            b_contar += 1
            
    print (f"{a_contar}\n{b_contar}")
    

if __name__ == "__main__":
    
    primeira_multipla_entrada = input().rstrip().split()
    
    s = int(primeira_multipla_entrada[0])
    
    t = int(primeira_multipla_entrada[1])
    
    segunda_multipla_entrada = input().rstrip().split()
    
    a = int(segunda_multipla_entrada[0])
    
    b = int(segunda_multipla_entrada[1])
    
    terceira_multipla_entrada = input().rstrip().split()
    
    m = int(terceira_multipla_entrada[0])
    
    n = int(primeira_multipla_entrada[1])
    
    macas = list(map(int, input().rstrip().split()))
    
    laranjas = list(map(int, input().rstrip().split()))
    
    countApplesAndOranges(s, t, a, b, macas, laranjas)