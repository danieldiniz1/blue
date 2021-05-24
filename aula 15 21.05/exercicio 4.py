def contador(inicio,fim,passo):
    for cont in range(1,11):
        print(cont)
    print()
    for cont2 in range(10,-1,-2):
        print(cont2)
    print()
    for cont3 in range(inicio,fim,passo):
        print(cont3)
inicio= int(input("digite um nº para iniciar: "))
fim = int(input("digite um nº para finalizar: "))
passo= int(input("digite o nº de passos que o programa vai dar: "))
contador(inicio,fim,passo)
