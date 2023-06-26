from decentNumber import decentNumber

if __name__ == '__main__':
    
    t = int(input().strip())
    
    for t_itr in range(t):
        
        n = int(input().strip())
        
        res = decentNumber(n)
        
        print(res)