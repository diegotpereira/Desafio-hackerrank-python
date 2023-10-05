from gridChallenge import gridChallenge

if __name__ == '__main__':
    
    t = int(input())
    
    for itr in range(t):
        
        n = int(input().strip())
        grade = []
        
        for _ in range(n):
            
            grade_item = input()
            grade.append(grade_item)
            
        resultado = gridChallenge(grade)
        
        print(resultado + '\n')