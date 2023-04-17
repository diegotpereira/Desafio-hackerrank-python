

def girarArray(arr, k):
    
    # arr = [5, 6, 7]
    # k = 2
    
    for i in range(k):
        
        ultimo = arr.pop()
        
        arr.insert(0, ultimo)    
    
    return arr
