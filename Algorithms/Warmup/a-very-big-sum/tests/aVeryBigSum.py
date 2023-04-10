def aVeryBigSum(ar):
    
    return sum(ar)

if __name__ == '__main__':
    
    ar_contar = int(input).strip()
    
    ar = list(map(int, input().rstrip().split()))
    
    resultado = aVeryBigSum(ar)
    
    print(' '.join(map(str, resultado)))