# exercício de while 

opc = 1

while opc == 1:
    numero = float(input("digite um numero: "))
    print()
    if (numero == 0):
        print(f'o numero digitado é: {numero}')
        print()
    elif (numero > 0):
        print(f'o numero {numero:.2f} é positivo')
        print()
    else:
        print(f'o numero {numero:.2f} é negativo')
        print()
    resposta = input("você deseja continuar? (sim/não) ")
    print()
    if resposta =="não":
        opc = 0
        print("programa finalizado")