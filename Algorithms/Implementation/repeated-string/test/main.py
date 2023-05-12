from repeatedString import repeatedString

if __name__ == "__main__":
    
    s = input()
    n = int(input().strip())
    
    resultado = repeatedString(s, n)
    
    print(resultado + '\n')