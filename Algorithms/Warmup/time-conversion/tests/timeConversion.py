import datetime as dt

# def timeConversion(s):
    
#     # verifica se é AM
#     if (s.__contains__("AM")):
        
#         # se hora é 12AM retorna 00:00:00
#         if(s[0:2] == "12"):
            
#             return "00" + s[2:8]
#         # caso contrário, retorna a hora sem alteração
#         return s[0:8]
    
#     # verifica se é PM
#     if (s.__contains__("PM")):
        
#         # se hora é 12PM, retorna a hora sem alteração
#         if(s[0:2] == "12"):
            
#             return s[0:8]
        
#         # caso contrário, adiciona 12 horas à hora atual
#         else:
            
#             mudar = int(s[0:2]) + 12
            
#             return str(mudar) + s[2:8]


# def timeConversion(s):
    
#     # Separa a hora, minuto e segundo a partir da string de entrada.
#     hora, minuto, segundo = map(int, s[:-2].split(':'))
#     # Separa o "AM" ou "PM" a partir da string de entrada.
#     mediano = s[-2:]
    
#     # Se for "AM" e a hora for 12, define a hora como 0.
#     if mediano == 'AM' and hora == 12:
        
#         hora = 0
#     # Se for "PM" e a hora for diferente de 12, adiciona 12 horas à hora atual.
#     elif mediano == 'PM' and hora != 12:
        
#         hora += 12
        
#     # Retorna a hora, minuto e segundo em formato de string, 
#     # com 2 dígitos para hora, minuto e segundo, respectivamente.
#     return f'{hora:02d}:{minuto:02d}:{segundo:02d}'

def timeConversion(s):
    # Usando a biblioteca datetime para converter a string em um objeto datetime
    tempo = dt.datetime.strptime(s, '%I:%M:%S%p')
    
    # Usando o método strftime para converter o objeto datetime em uma string com o formato desejado
    tempo = tempo.strftime('%H:%M:%S')
    
    # Retorna a string com o formato desejado
    return tempo
    

if __name__ == "__main__":
    
    s = input()
    
    resultado = timeConversion(s)
    
    print(resultado + '\n')