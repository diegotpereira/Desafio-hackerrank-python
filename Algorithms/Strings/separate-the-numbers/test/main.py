from separateNumbers import separateNumbers

if __name__ == '__main__':
    
    q = int(input().strip())
    
    for qItr in range(q):
        
        s = input()
        
        separateNumbers(s)