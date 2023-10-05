from marcsCakewalk import marcsCakewalk

if __name__ == '__main__':
    
    n = int(input().strip())
    
    calorias = list(map(int, input().rstrip().split()))
    
    resultado = marcsCakewalk(calorias)
    
    print(str(resultado) + '\n')