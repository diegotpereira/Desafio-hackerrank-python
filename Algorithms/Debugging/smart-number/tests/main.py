from is_smart_number import is_smart_number

# Lê o número de casos de teste.
for _ in range(int(input())):
    # Lê o número para verificar se é um "Smart Number".
    num = int(input())
    # Chama a função 'is_smart_number' e armazena o resultado em 'ans'.
    ans = is_smart_number(num)
    # Imprime "YES" se 'ans' for True, caso contrário, imprime "NO".
    if ans:
        print("YES")
    else:
        print("NO")
