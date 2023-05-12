from libraryFine import libraryFine

if __name__ == "__main__":
    
    primeiraMultiplaEntrada = input().rstrip().split()
    
    d1 = int(primeiraMultiplaEntrada[0])
    m1 = int(primeiraMultiplaEntrada[1])
    y1 = int(primeiraMultiplaEntrada[2])
    
    segundaMultiplaEntrada = input().strip().split()
    
    d2 = int(segundaMultiplaEntrada[0])
    m2 = int(segundaMultiplaEntrada[1])
    y2 = int(segundaMultiplaEntrada[2])
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    print(str(resultado) + '\n')