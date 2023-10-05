from findMedian import findMedian

if __name__ == '__main__':
    
    tamanhoArray = int(input().strip())
    
    arr = list(map(int, input().rsplit().split()))
    
    resultado = findMedian(arr)
    
    print(str(resultado + '\n'))