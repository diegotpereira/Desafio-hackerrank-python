# def dayOfProgrammer(year):
    
#     # Verifica se o ano é anterior a 1918.
#     if year < 1918:
        
#         # Se o ano for divisível por 4
#         if year % 4 == 0:
            
#             # se for retorna o dia 12/09 e o ano.
#             return '12.09.' + str(year)
        
#         else:
            
#             # se não for retorna o dia 13/09 e o ano.
#             return '13.09.' + str(year)
        
#     # Verifica se o ano é posterior a 1918.
#     elif year > 1918:
        
#         # Se o ano for divisível por 400 ou por 4 mas não por 100
#         if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

#             # se for retorna o dia 12/09 e o ano.
#             return '12.09.' + str(year)
        
#         else: 
            
#             # Caso contrário, retorna o dia 13/09 e o ano.
#             return '13.09.' + str(year)
        
#     else:
        
#         # Para o ano de 1918, retorna o dia 26/09 e o ano.
#         return '26.09.1918'
    
# def dayOfProgrammer(ano):
    
#     # Define o dia e o mês padrão para o Dia do Programador.
#     d = "13"
#     m = "09"
    
#     # Verifica se o ano é 1918, que teve uma data específica para o Dia do Programador.
#     if ano == 1918:
        
#         # em 1918 o Dia do Programador naquele ano foi comemorado em 26 de setembro (13 dias depois do dia 256). 
#         d = "26"
        
#     # Verifica se o ano é anterior a 1918 e divisível por 4.
#     elif ano < 1918 and ano % 4 == 0:
        
#         # A variável d é definida como "12" quando o ano é anterior a 1918 ou posterior a 1918 e é um ano bissexto.
#         d = "12"
        
#     # Verifica se o ano é posterior a 1918 e é um ano bissexto de acordo com as regras gregorianas.
#     elif ano > 1918 and ((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)):
        
#         # A variável d é definida como "12" quando o ano é anterior a 1918 ou posterior a 1918 e é um ano bissexto.
#         d = "12"
    
#     # Retorna a data do Dia do Programador formatada.
#     return ("{}.{}.{}".format(d, m, ano))

def dayOfProgrammer(ano):
    
    # Define o dia do ano que é o dia do programador
    dias = 256
    
    # Define a quantidade de dias de cada mês em um dicionário
    meses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    # Inicializa variáveis para o mês e acumulador de dias
    mes = 0
    acum_dias = 0
    
    for i, v in meses.items():
        
        # Verifica se o ano é menor ou igual a 1917
        if ano <= 1917:
            
            # Verifica se é um ano bissexto
            if ano % 4 == 0:
                
                # se for atualiza a quantidade de dias de fevereiro
                meses[2] = 29
                
        # Verifica se o ano é maior ou igual a 1919
        elif ano >= 1919:
            
            # Verifica se é um ano bissexto
            if ano % 400 == 0: 
                
                # se for atualiza a quantidade de dias de fevereiro
                meses[2] = 29
            elif ano % 4 == 0 and ano % 100  != 0:
                meses[2] = 29
                
        # Se o ano for igual a 1918
        elif ano == 1918:
            
            # Subtrai 13 dias de fevereiro para ajustar o calendário
            meses[2] -= 13
        
        # Acumula a quantidade de dias do mês atual
        acum_dias += v
        
        # Se o acumulador for maior ou igual ao dia do programador
        if acum_dias >= dias:
            
            # atualiza o mês e sai do loop
            acum_dias -= v
            mes = i
            break
    
     # Calcula o dia do programador subtraindo o acumulador do dia atual
    dia = dias - acum_dias
    
    # Retorna a data formatada com zero à esquerda no dia e no mês
    return f"{dia:02d}.{mes:02d}.{ano}"




if __name__ == "__main__":
    
    ano = int(input().strip())
    
    resultado = dayOfProgrammer(ano)
    
    print(resultado + '\n')