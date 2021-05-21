from time import sleep
n1 = int(input("Digite o 1 nº: "))
n2 = int(input("Digite o 2 nº: "))
print()
sleep(1)
sair = False

while sair == False:
    print("menu", "\n", "[ 1 ] somar", "\n", "[ 2 ] multiplicar", "\n", "[ 3 ] maior", "\n", "[ 4 ] novos números", "\n", "[ 5 ] sair do programa")
    print()
    sleep(1)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print(f"o 1º número é: {n1}, o 2º número é: {n2}.")
        print("O total da soma é: ",n1+n2)
        print()
        sleep(1)
    elif opcao ==2:
        print(f"o 1º número é: {n1}, o 2º número é: {n2}.")
        print("A multiplicação dos números é: ",n1*n2)
        print()
        sleep(1)
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            print(f"o 1º número é: {n1}, o 2º número é: {n2}.")
            print("O maior número é: ", n2)
            print()
            sleep(1)
        else:
            print(f"o 1º número é: {n1}, o 2º número é: {n2}.")
            print("O maior número é: ", n1)
            print()
            sleep(1)
    elif opcao == 4:
        n1 = int(input("Digite o 1 nº: "))
        sleep(1)
        n2 = int(input("Digite o 2 nº: "))
    elif opcao ==5:
        print("Programa finalizado!")
        sair = True
    
