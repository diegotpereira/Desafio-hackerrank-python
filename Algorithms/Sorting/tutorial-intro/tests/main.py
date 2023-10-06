from introTutorial import introTutorial

if __name__ == '__main__':
    
    V = int(input().strip())
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = introTutorial(V, arr)
    
    print(str(resultado) + '\n')