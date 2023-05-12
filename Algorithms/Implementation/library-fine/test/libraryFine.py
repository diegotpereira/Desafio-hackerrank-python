# A tarefa do problema "Library Fine" é calcular a multa 
# a ser paga por um livro devolvido atrasado em uma biblioteca, 
# com base nas seguintes regras:

# Se o livro for devolvido no mesmo ano em que foi emprestado, 
# não há multa a ser paga.
# Se o livro for devolvido após o ano em que foi emprestado, 
# mas dentro do mesmo mês e ano em que foi emprestado, a multa 
# é calculada multiplicando o número de dias de atraso pelo valor 
# fixo diário da multa.
# Se o livro for devolvido após o mês e ano em que foi emprestado, 
# mas dentro do mesmo ano, a multa é calculada multiplicando o 
# número de meses de atraso pelo valor fixo mensal da multa.
# Se o livro for devolvido após o ano em que foi emprestado, a 
# multa é fixa e igual a 10000.
# O objetivo é implementar uma função que receba as datas de 
# empréstimo e devolução do livro e retorne o valor da multa a 
# ser paga.


# def libraryFine (d1, m1, y1, d2, m2, y2):
    
#     # Se o ano de devolução for menor que o ano previsto, 
#     if (y1 < y2):
        
#         # a multa é zero
#         return 0
        
#     # Se o dia de devolução for maior que o dia previsto 
#     # e o mês e ano forem os mesmos,
#     elif(d1 > d2 and m1 == m2 and y1 == y2):
        
#         # a multa é calculada multiplicando 
#         # a diferença de dias por 15
#         return 15 * (d1 - d2)
        
#     # Se o mês de devolução for maior que o mês 
#     # previsto e o ano for o mesmo, 
#     elif(m1 > m2 and y1 == y2):
        
#         # a multa é um valor fixo de 500
#         return 500 * (m1 - m2)
    
#     # Se o ano de devolução for maior que o ano previsto,
#     elif (y1 > y2):
        
#         # a multa é um valor fixo de 10000
#         return 10000
        
#     # Caso contrário, 
#     else:
        
#         # a multa é zero
#         return 0



# def libraryFine (d1, m1, y1, d2, m2, y2):
    
#     # Calcula a multa com base nas diferenças entre as datas fornecidas
#     # e as datas previstas de devolução
    
#     # Verifica se o ano de devolução é maior que o ano previsto
#     ano = (y1 - y2) * 10000 if y1 > y2 else 0
    
#     # Verifica se o mês de devolução é maior que o mês previsto
#     # e se o ano é o mesmo
#     mes = (m1 - m2) * 500 if m1 > m2 and y1 == y2 else 0
    
#     # Verifica se o dia de devolução é maior que o dia previsto,
#     # se o mês é o mesmo e se o ano é o mesmo
#     dia = (d1 - d2) * 15 if d1 > d2 and m1 == m2 and y1 == y2 else 0
    
#     # Retorna a soma das multas calculadas
#     return ano + mes + dia

import datetime

def libraryFine (d1, m1, y1, d2, m2, y2):
    
    # Converte as datas de saída e devolução em objetos de data
    saida = datetime.date(y1, m1, d1)
    devolucao =  datetime.date(y2, m2, d2)
    
    # Verifica se a data de saída é menor 
    # ou igual à data de devolução
    if(saida <= devolucao):
        
        # Caso a data de saída seja anterior 
        # ou igual à data de devolução,
        # não há multa a ser aplicada
        return 0
    
    # Caso contrário, é necessário calcular a multa
    else:
        
        # Verifica se o mês de devolução é igual ao mês de saída,
        # se o ano de devolução é igual ao ano de saída
        # e se o dia de saída é maior que o dia de devolução
        if m2 == m1 and y1 == y2 and d1 > d2:

            # Calcula a multa com base no número de dias de atraso
            return 15 * (d1 - d2)
        
        # Verifica se o ano de devolução é igual ao ano de saída
        # e se o mês de devolução é menor que o mês de saída
        elif y1 == y2 and m1 > m2:
            
            # Calcula a multa com base no número de meses de atraso
            meses = m1 - m2
            
            return 500 * meses
        
        else:
            
            # Caso não se enquadre nas condições anteriores,
            # a multa é fixa em 10000
            return 10000