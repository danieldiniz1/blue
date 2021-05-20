def dia1(dia) :
    dia2= ['', "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e treis", "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um"]
    dia3 =dia2[dia]
    if dia > 0 and dia <= 31 :
      return dia3 
    else:
      return "Null"   

def mes1(mes) :
    mes2 = ['','janeiro','fevereiro','março','abril','maio',
    'junho','julho','agosto','setembro','novembro','dezembro']
    mes3 = mes2[mes]
    if mes > 0 and mes <= 12:
        return mes3
    else:
        return "Null"

def ano1(ano) :
    ano2 = ["um mil  novecentos e noventa", "um mil  novecentos e noventa e um", "um mil novecentos e noventa e dois", "um mil novecentos e noventa e tres", "um mil noveventos e noventa e quatro", "um mil novecentos e noventa e cinco", "um mil novecentos e noventa e seis", "um mil novecentos e noventa e sete", "um mil novecentos e noventa e oito", 'um mil novecentos e noventa e nove', "dois mil", "dois mil e um", "doi mil e dois", "dois mil e tres", "doi mil e quatro", "dois mil e cinco", "dois mil e seis", "dois mil e sete", "dois mil e oito", 'dois mil e nove', "dois mil e dez", "dois mil e onze", "dois mil e doze", "dois mil e treze", "doi mil e quatorze", "dois mil e quinze", "doi mil e dezeseis", "dois mil e dezesete", "dois mil e dezoito", "dois mil e dezenove", "doi mil e vinte", "doi mil e vinte e um"]
    
    if ano >= 1990 and ano <= 2021:
        return ano
    else:
        return "Null"    
    
    
dia = int(input('Entre com dia :'))    
mes = int(input('Entre com mes :'))    
ano = int(input('Entre com ano  :'))    

dia1(dia)
mes1(mes)
ano1(ano)

print(f"A data digitada é : {dia1(dia)} de {mes1(mes)} de {ano1(ano)} ")
