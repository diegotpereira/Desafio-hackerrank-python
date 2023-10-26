# O problema "Password Cracker" no HackerRank 
# é um desafio relacionado à quebra de senhas. 
# O objetivo é criar um programa que, dadas uma 
# lista de senhas e uma senha codificada, determine 
# se é possível formar a senha codificada pela 
# concatenação de uma ou mais senhas da lista. 
# Se for possível, o programa deve retornar a 
# lista de senhas usadas para formar a senha codificada.

# O problema envolve uma série de passos, 
# incluindo a decodificação da senha codificada 
# e a busca pelas combinações de senhas na lista 
# que formam a senha codificada. O desafio é 
# implementar uma solução eficiente para determinar 
# se é possível ou não formar a senha codificada 
# e, se possível, retornar a lista de senhas usadas.

# def passwordCracker(passwords, loginAttempt):
    
#     # Crie uma tabela para armazenar as possíveis combinações de senhas
#     tab = [None] * (len(loginAttempt) + 1)
#     tab[0] = ""
    
#     for i in range(1, len(loginAttempt) + 1):
        
#         # Percorra as senhas disponíveis
#         for pwd in passwords:
            
#             k = i - len(pwd)
            
#             # Verifique se a substring do loginAttempt (k:i) coincide com a senha
#             if loginAttempt[k:i] == pwd:
                
#                 # Se a combinação anterior (tab[k]) existe, atualize a tabela com a nova combinação
#                 if tab[k] is not None:
                    
#                     tab[i] = f"{tab[k]} {loginAttempt[k:i]}"
                    
#                     break 
                
#     # A combinação final está na última posição da tabela
#     saida = tab[-1]
    
#     # Se não houver combinação, retorne "WRONG PASSWORD"
#     if saida is None:
        
#         return "WRONG PASSWORD"
    
#     # Caso contrário, retorne a combinação de senhas
#     else:
        
#         return saida.strip()
    

def passwordCracker(passwords, loginAttempt):
    
    if loginAttempt == "":
        
        return 
    return