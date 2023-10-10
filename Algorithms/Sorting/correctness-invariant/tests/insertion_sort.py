# Neste problema, você é apresentado a um código de ordenação 
# incorreto e é solicitado a corrigi-lo usando um loop invariante.

# Aqui está um resumo da tarefa:

# Dado um array de inteiros, você precisa implementar uma 
# versão correta do algoritmo de ordenação Insertion Sort, 
# que deve ordenar o array em ordem crescente. O algoritmo 
# fornecido inicialmente no problema está incorreto e requer correção.

# A parte crucial deste problema é entender e implementar um 
# loop invariante para garantir que o algoritmo funcione corretamente.

# Um loop invariante é uma propriedade que é verdadeira toda 
# vez que o programa atinge um ponto específico em seu ciclo, 
# independentemente do número de iterações que ocorreram anteriormente.

def insertion_sort(l):
    
    # Loop através de todos os elementos do array, exceto o último.
    for i in range(len(l) - 1):
        
        j = i
        
        # key = l[i]
        
        # Comece um loop enquanto 'j' for maior ou igual a 0 e o elemento à direita for maior que o elemento à esquerda.
        while (j >= 0) and (l[j] > l[j + 1]):
        
            # Troque os elementos adjacentes, movendo o elemento maior para a direita.
            l[j + 1], l[j] = l[j], l[j + 1]
        
            # Decrementa 'j' para verificar o próximo par de elementos à esquerda.
            j -= 1
        
        
        # l[j + 1] = key
   
    return l
