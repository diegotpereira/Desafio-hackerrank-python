from gemstones import gemstones

if __name__ == '__main__':
    
    n = int(input().strip())
    arr = []
    
    for _ in range(n):
        
        arr_item = input()
        arr.append(arr_item)
        
    resultado = gemstones(arr)
    
    print(str(resultado) + '\n')