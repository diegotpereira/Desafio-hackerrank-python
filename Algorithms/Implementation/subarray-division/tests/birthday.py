

# def birthday(s, d, m):
    
#     # Calcula a duração da primeira sequência de `m` números.
#     duracao = sum(s[:m])
    
#     # Se a duração da primeira sequência for igual a `d`, incrementa o contador em 1.
#     # Caso contrário, mantém o contador em 0.
#     contar = 1 if duracao == d else 0
    
#     # Itera sobre o restante da lista `s`, a partir do índice `m`.
#     for i in range(m, len(s)):
        
#         # Atualiza a duração subtraindo o primeiro número da sequência anterior e
#         # adicionando o próximo número da lista `s`.
#         duracao += s[i] - s[i -m]
        
#         # Se a duração da nova sequência for igual a `d`, incrementa o contador em 1.
#         if duracao == d:
            
#             contar += 1
            
#     # Retorna o valor final do contador.
#     return contar

# def birthday(s, d, m):
    
#     # Verifica se o tamanho da lista `s` é igual a `m`.
#     if len(s) == m:
        
#         # Se sim, verifica se a soma dos elementos da lista `s` é igual a `d`.
#         if sum(s) == d:
            
#             # Se sim, retorna 1 (ou seja, a sequência é válida).
#             return 1
        
#         else:
            
#             # Se não, retorna 0 (ou seja, a sequência é inválida).
#             return 0
        
#     # Se o tamanho da lista `s` for maior que `m`, chama recursivamente a função `birthday`
#     # para verificar as subsequências de tamanho `m` que começam em diferentes posições da lista.
#     # Para isso, divide a lista `s` em duas: uma contendo os primeiros `m` elementos, e outra
#     # contendo o restante. Em seguida, soma o resultado das chamadas recursivas para cada uma
#     # dessas sublistas.
#     return birthday(s[:m], d, m) + birthday(s[1:], d, m)


def birthday(s, d, m):
    
    # Inicializa a variável `contar` com zero.
    contar = 0
    
    # Percorre a lista `s` de índice 0 até o índice len(s) - 1.
    for i in range(0, len(s)):
        
        # Verifica se é possível selecionar uma sequência de `m` elementos começando no índice `i`.
        if i + m <= len(s):
            
            # Se sim, soma os elementos da sequência.
            res = 0
            
            # A variável i é o índice do primeiro elemento da sublista, 
            # e i + m é o índice do elemento após o último elemento da sublista.
            for j in range(i, i + m):
                
                res = res + s[j]
                
            # Verifica se a soma dos elementos é igual a `d`.
            if res == d:
                
                # Se sim, incrementa a variável `contar`.
                contar += 1
                
    # Retorna o valor final de `contar`.
    return contar

if __name__ == "__main__":
    
    n = int(input().strip())
    
    s = list(map(int, input().rstrip().split()))
    
    primeira_multipla_entrada = input().rstrip().split()
    
    d = int(primeira_multipla_entrada[0])
    
    m = int(primeira_multipla_entrada[1])
    
    resultado = birthday(s, d, m)
    
    print(str(resultado) + '\n')