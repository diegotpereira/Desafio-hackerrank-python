# Marc adora cupcakes, mas ele também gosta de 
# se exercitar. Ele começa seu dia com uma 
# xícara de café e depois caminha uma certa 
# distância para queimar calorias. Marc pode 
# fazer um passo de tamanho variável.

# Além disso, Marc gosta de comer seus 
# cupcakes em ordem do menor para o maior. 
# Uma vez que ele começa a comer um cupcake, 
# ele não pode parar até que tenha comido o
# cupcake inteiro. Ele pode pegar o cupcake 
# de menor caloria que ele tem disponível, 
# comer e fazer mais alguns passos, em seguida, 
# pegar o próximo cupcake mais calórico e assim 
# por diante, até que tenha comido todos os cupcakes.

# Marc gosta de escolher um caminho que minimiza 
# a quantidade de calorias que ele queima durante 
# a caminhada para comer seus cupcakes. Dado que 
# as calorias queimadas são proporcionais ao 
# quadrado do tamanho do passo, ele tenta fazer 
# passos menores ao comer cupcakes de alta caloria 
# para evitar queimar muitas calorias.

# Dado o número de calorias em cada um dos 
# cupcakes, você precisa determinar o número 
# mínimo de passos que Marc deve tomar para 
# comer todos os cupcakes.

# def marcsCakewalk(caloria):
    
#     # Ordenando a lista de calorias 
#     # em ordem decrescente
#     caloria.sort(reverse = True)
    
#     # Inicializando a variável min_passos 
#     # para contar os passos mínimos
#     min_passos = 0
    
#     # Iterando sobre as calorias usando 
#     # enumerate para obter o índice e o valor
#     for i, calorias in enumerate(caloria):
        
#         # Calculando os passos mínimos usando 
#         # a fórmula e adicionando ao total
#         min_passos += calorias * (2 ** i)
        
#     # Retornando o resultado dos passos mínimos
#     return min_passos


# def marcsCakewalk(caloria):
    
#     # Usando a função sorted para ordenar as calorias em ordem decrescente
#     # e, em seguida, aplicando a função enumerate para obter o índice e o valor de cada elemento
#     # da lista ordenada
#     # Isso nos permitirá calcular os passos mínimos ponderados para cada cupcake
#     # enquanto eles são consumidos em ordem decrescente de calorias
#     return sum([(2 ** i) * w for i, w in enumerate(sorted(caloria, reverse=True))])

def marcsCakewalk(caloria):
    
    # Ordenando as calorias em ordem decrescente 
    # usando a função sorted
    caloria = sorted(caloria, reverse=True)
    
    # Inicializando a variável total para 
    # armazenar os passos mínimos
    total = 0
    
    # Iterando sobre os índices da 
    # lista ordenada de calorias
    for indice in range(len(caloria)):
        
        # Calculando a contribuição ponderada do 
        # cupcake atual para os passos mínimos
        # Multiplicando as calorias do cupcake pelo 
        # valor de 2 elevado ao índice
        total += (2 ** indice) * caloria[indice]
        
    # Retornando o resultado final dos passos mínimos
    return total