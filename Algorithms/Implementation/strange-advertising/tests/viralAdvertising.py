# O problema da estratégia de publicidade viral da HackerLand Enterprise é resolvido utilizando um loop while, que simula a propagação do anúncio ao longo dos dias. A cada dia, o número de pessoas que recebem o anúncio é igual ao número de pessoas que curtiram o anúncio no dia anterior, multiplicado por 3 e dividido por 2. A metade desse número é o número de pessoas que curtirão o anúncio no dia atual.

# Inicialmente, o número de pessoas que recebem o anúncio é igual a 5, então no primeiro dia, a metade desse número (2) é o número de pessoas que curtem o anúncio. Esse valor é armazenado em uma variável total. Em cada iteração do loop while, o número de pessoas que curtem o anúncio é adicionado a essa variável total. O loop while é executado por n dias, e o valor final de total é retornado como resultado.

# A lógica por trás do problema é a seguinte:

# No primeiro dia, 5 pessoas recebem o anúncio.
# Metade dessas pessoas (ou seja, 2) curtem o anúncio e compartilham com seus amigos, que totalizam 3 pessoas.
# No segundo dia, 3 pessoas recebem o anúncio.
# Metade dessas pessoas (ou seja, 1) curtem o anúncio e compartilham com seus amigos, que totalizam 1.5 pessoas.
# No terceiro dia, 1.5 pessoas recebem o anúncio (arredondado para baixo para 1).
# Metade dessas pessoas (ou seja, 0.5) curtem o anúncio e compartilham com seus amigos, que totalizam 0.75 pessoas.
# No quarto dia, 0.75 pessoas recebem o anúncio (arredondado para baixo para 0).
# O processo continua para os próximos dias.
# O resultado final é a soma total de todas as pessoas que curtiram o anúncio em todos os dias considerados.

# def viralAdvertising(n):
    
#     # número de pessoas que curtem o anúncio no último dia
#     curtida = 0
    
#     # número de pessoas que recebem o anúncio no primeiro dia
#     commpartilhado = 5
    
#     # número total de pessoas que curtiram o anúncio até o momento
#     total = 0
    
#     while n > 0:
        
#         # Calcula o número de pessoas que curtiram o anúncio no último dia
#         curtida = commpartilhado // 2
        
#         # Adiciona o número de pessoas que curtiram o anúncio no último dia ao total
#         total += curtida
        
#         # Calcula o número de pessoas que receberão o anúncio no próximo dia
#         commpartilhado = 3 * curtida
        
#         # Decrementa o contador de dias
#         n -= 1
    
#     # Retorna o número total de pessoas que curtiram o anúncio até o momento
#     return total

# import math


# def viralAdvertising(n):
    
#     # começa com 5 pessoas recebendo o anúncio no primeiro dia
#     compartilhado = 5
#     # inicia a variável acumulativo com 0
#     acumulativo = 0
    
#     # loop for para simular a propagação do anúncio nos dias
#     # 1 representa o primeiro dia
#     # n + 1 representa o dia seguinte ao último dia que deve ser considerado na contagem.
#     for i in range(1, n + 1):
        
#         # se não for o primeiro dia, 
#         if i > 1:
            
#             # o número de pessoas que compartilham o anúncio é igual ao 
#             # número de curtidas do dia anterior multiplicado por 3
#             compartilhado = curtida * 3
            
#         # metade das pessoas que recebem o anúncio irão curtir
#         curtida = math.floor(compartilhado / 2)
        
#         # adiciona o número de pessoas que curtiram o anúncio a variavel acumulativo
#         acumulativo += curtida
        
#     # retorna o número acumulado de pessoas que curtiram o anúncio
#     return acumulativo


# def viralAdvertising(n):
    
#     # Inicializa a lista compartilhado com um único elemento, 5
#     compartilhado = [5]
    
#     # Inicializa a lista curtido com o número de pessoas que curtem o anúncio no primeiro dia
#     curtido = [5//2] 
    
#     # Loop para calcular o número de pessoas que curtem o anúncio em cada dia
#     for i in range(n - 1):
        
#         # Adiciona o número de pessoas que compartilham o anúncio no dia i à lista compartilhado
#         compartilhado.append(curtido[i] * 3)
        
#         # Calcula o número de pessoas que curtem o anúncio no dia i+1 e adiciona à lista curtido
#         curtido += [compartilhado[i + 1] // 2]
        
#     # Retorna o número total de pessoas que curtiram o anúncio
#     return sum(curtido)


def viralAdvertising(n):
    
    compartilhado = 5
    curtido = [5 // 2]
    
    for i in range(n -1):
        
        compartilhado = curtido[i] * 3
        curtido += [compartilhado // 2]
        
    return sum(curtido)

if __name__ == "__main__":
    
    n = int(input().strip())

    resultado = viralAdvertising(n)

    print(str(resultado) + '\n')
    
        