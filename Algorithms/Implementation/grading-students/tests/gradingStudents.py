# def gradingStudents(grades):
    
#     # loop através das notas de estudantes
#     for i in range(0, len(grades)):
        
#         # se a nota é menor que 38, não há necessidade de arredondar
#         if grades[i] < 38:
            
#             continue
        
#         else:
#             # pegue a nota e encontre o resto da divisão por 5
#             temp = grades[i]
#             te = temp % 5
            
#             # se o resto for 3, arredonde a nota para cima adicionando 2 pontos
#             if te == 3:
                
#                 temp = temp + 2
#                 grades[i] = temp 
            
#             # se o resto for 4, arredonde a nota para cima adicionando 1 ponto
#             elif te == 4:
                
#                 temp = temp + 1
#                 grades[i] = temp
            
#             # se o resto for 0, 1 ou 2, não há necessidade de arredondar
#             else:
#                 continue
            
#     # retorne as notas atualizadas        
#     return grades

import math


def gradingStudents(grades):
    
    # Crie uma lista vazia para as notas arredondadas
    grades_arredondadas = list()
    
    # Itere por cada nota na lista de notas de entrada
    for grade in grades:
        
        # Calcule a próxima múltiplo de 5 após a nota atual
        n = math.ceil(grade / 5)
        r = n * 5
        
        # Calcule a diferença entre o próximo múltiplo de 5 e a nota atual
        g = r - grade
        
        # Se a diferença for menor que 3 e a nota atual for maior ou igual a 38,
        # arredonde a nota adicionando a diferença ao valor da nota atual
        if g < 3 and grade >= 38:
            
            grades_arredondadas.append(grade + g)
        
        # Caso contrário, mantenha a nota inalterada
        else:
            
            grades_arredondadas.append(grade)
            
    # Retorne a lista de notas arredondadas
    return grades_arredondadas
    
if __name__ == "__main__":
    
    contar_grade = int(input().strip())
    
    grades = []
    
    for _ in range(contar_grade):
        
        grades_item = int(input().strip())
        grades.append(grades_item)
        
    resultado = gradingStudents(grades)
    
    print('\n'.join(map(str, resultado)))