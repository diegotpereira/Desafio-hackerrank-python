import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    # Soma os elementos do array
    return sum(ar)

if __name__ == '__main__':
    # Lê o tamanho do array
    ar_count = int(input().strip())

    # Lê os elementos do array
    ar = list(map(int, input().rstrip().split()))

    # Chama a função para somar o array
    result = simpleArraySum(ar)

    # Imprime o resultado
    print(result)
