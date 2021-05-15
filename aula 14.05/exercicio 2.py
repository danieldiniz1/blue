opc = 0

while opc == 0:
    senha = input("digite a senha: ")
    print()
    if senha == "gabriel123":
        opc = 1
        print("senha correta")
    else:
        while senha != "gabriel123":
            print()
            print("senha incorreta")
            print()
            senha = input("digite a senha: ")
            print()
            if senha =="gabriel123":
                opc =1
                print("senha correta")
                print()