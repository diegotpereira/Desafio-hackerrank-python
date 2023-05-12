from jumpingOnClouds import jumpingOnClouds

if __name__ == "__main__":
    
    n = int(input().strip())
    
    c = list(map(int, input().rstrip().split()))
    
    resultado = jumpingOnClouds(c)
    
    print(str(resultado) + '\n')