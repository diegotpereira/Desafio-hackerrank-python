# def designerPdfViewer(h, word):
    
#     # Encontrar a altura máxima das letras presentes na sequência selecionada
#     altura_letra_mais_alta = max([h[ord(c) - ord('a')] for c in word])
    
#     # Calcular a área do retângulo destacado
#     area = altura_letra_mais_alta * len(word)
    
#     return area

# def designerPdfViewer(h, word):
    
#     # Inicializa a altura máxima com 0
#     maxima_altura = 0
    
#     # Percorre cada letra da palavra
#     for i in word:
        
#         # Obtém a altura da letra atual a partir do array h usando a função ord() 
#         # para obter o valor ASCII da letra e subtraindo 97 para obter o índice correspondente no array
#         x = h[ord(i) - 97]  
        
#         # Atualiza a altura máxima se a altura da letra atual for maior
#         if (x > maxima_altura):
            
#             maxima_altura = x 
            
#     # Retorna a área da palavra destacada multiplicando a altura máxima pelo comprimento da palavra
#     return len(word) * maxima_altura


def designerPdfViewer(h, word):
    
    # Define a string com o alfabeto em ordem alfabética
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    # Cria uma lista com os índices correspondentes a cada letra da palavra na string abc
    indice_lista = [abc.index(x) for x in word]
    
    # Cria uma lista com as alturas correspondentes a cada letra da palavra usando os índices obtidos na linha anterior e o array h
    altura = [h[x] for x in indice_lista]
    
    # Retorna a área da palavra destacada multiplicando a altura máxima pelo comprimento da palavra
    return max(altura) * len(word)

if __name__ == "__main__":
    
    altura_letra = list(map(int, input().rstrip().split()))

    word = input()

    resultado = designerPdfViewer(altura_letra, word)

    print(str(resultado) + '\n')