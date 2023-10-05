from cavityMap import cavityMap

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    grade = []
    
    for _ in range(entrada):
        
        grade_item = input()
        grade.append(grade_item)
        
    resultado = cavityMap(grade)
    
    print('\n'.join(resultado))
    print('\n')
    
    