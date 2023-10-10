from insertion_sort import insertion_sort

if __name__ == '__main__':
    
    # Obtenha a entrada e realize a ordenação.
    m = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    resultado = insertion_sort(ar)

    # Imprima o array ordenado como uma string, separada por espaços.
    print(" ".join(map(str, ar)))
