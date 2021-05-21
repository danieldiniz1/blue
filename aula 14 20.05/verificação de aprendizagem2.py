
print()
vogais = 0
resposta = ""
continuar = True



while continuar == True:
    frase = input('Digite uma frase: ')
    print()
    for letra in frase:
        if letra in "aeiouAEIOU":
            vogais += 1
    for letra in frase:
        if not letra in('aeiouAEIOU'):
            resposta += letra 
    
    print("a frase sem as vogais é: ",resposta)
    print('A frase tem %d vogais ' %(vogais))
    print()
    resposta= "" 
    vogais = 0 
    
    continuar = input("você quer continuar? [sim/não] ")
    print()
    if continuar == "sim" or continuar == "SIM" or continuar =="s" or continuar == "S":
        continuar = True
    elif continuar == "não" or continuar == "NÃO" or continuar =="n" or continuar == "N":
        continuar == False
        print("Programa finalizado!")

