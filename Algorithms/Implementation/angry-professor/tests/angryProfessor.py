# Esta função verifica se um professor está irritado ou não com seus alunos
# de acordo com a quantidade de alunos que chegaram atrasados em uma determinada aula.
# Se o número de alunos que chegaram atrasados for menor que k, o professor não fica irritado
# e retorna 'YES'. Caso contrário, ele fica irritado e retorna 'NO'.

# def angryProfessor(k, a):
    
#     # inicializa o contador de alunos que chegaram atrasados
#     contar = 0
    
    
#     # percorre a lista de chegada dos alunos e incrementa o contador caso um aluno chegue atrasado
#     for i in range(len(a)):
        
#         if a[i] <= 0:
            
#             contar += 1
            
#     # verifica se a quantidade de alunos que chegaram atrasados é menor que k e retorna 'YES', 
#     # caso contrário, retorna 'NO'
#     return 'YES' if contar < k else 'NO'
        
        
# def angryProfessor(k, a):
    
#     # usa a função filter() para filtrar apenas os alunos que chegaram atrasados
#     #  parâmetro e retorna True se x for menor ou igual a zero, e False caso contrário. 
#     # Essa função é usada como argumento da função filter(), que filtra apenas os elementos 
#     # da lista a que atendem a essa condição
#     alunos_atrasados = list(filter(lambda x: x <= 0, a))
    
#     # verifica se a quantidade de alunos atrasados é menor que k e retorna 'YES', 
#     # caso contrário, retorna 'NO'
#     return 'YES' if len(alunos_atrasados) < k else 'NO'


def angryProfessor(k, a):
    
    # usa a compreensão de listas para criar uma lista apenas com os alunos que chegaram atrasados
    alunos_atrasados = [x for x in a if x <= 0]
    
    # verifica se a quantidade de alunos atrasados é menor que k e retorna 'YES', 
    # caso contrário, retorna 'NO'
    return 'YES' if len(alunos_atrasados) < k else 'NO'

if __name__ == "__main__":
    
    t = int(input().strip())

    for t_itr in range(t):
        primeira_multipla_entrada = input().rstrip().split()

        n = int(primeira_multipla_entrada[0])

        k = int(primeira_multipla_entrada[1])

        a = list(map(int, input().rstrip().split()))

        resultado = angryProfessor(k, a)

        print(resultado + '\n')