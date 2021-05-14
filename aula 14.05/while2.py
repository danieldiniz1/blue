


#for cont in range(1,60,2):
 #   print(cont)

#solução paulo
'''cont = -1
while cont <58:
    cont +=2
    print(cont)'''


# solução elias
'''cont = 0
while cont < 60:
    if cont % 2 != 0:
        print(cont)
    cont += 1'''
opc = 1
while opc ==1:

    num = 1
    contador = 1
    print()
    qtd = int(input("digite a quantidade de numeros impares desejados  "))
    print()
    numeros = []
    while contador <=qtd:
        print(num)
        numeros.append(num)
        contador = contador +1
        num = num +2
        
    print()
    numeros.reverse()
    print("tamanho da lista: ",len(numeros))
    print()
    print("lista: ",numeros)
    print()
    for i in numeros:
        print(i)

    continuar = input("você quer continuar? ").lower().strip()
    if continuar == "não" or continuar =="n" or continuar =="nao":
            opc = 0
            print()
            print("Programa finalizado!")
    elif continuar =="sim" or continuar == "s":
            opc =1
            print()
    else:
        while continuar != "não" and continuar != "não" and continuar != "sim" and continuar !="s" and continuar !="n":
            print("opção invalida!")
            print()
            continuar = input("Você quer continuar? ").lower().strip()
            if continuar == "não" or continuar == "nao" or continuar =="n":
                opc = 0
                print("programa finalizado!")