from time import sleep
from random import randint 

user = input("[cadastro] Digite seu nome de usuário: ")
sleep(1)
password = input("[cadastro] Digite sua senha: ")
sleep(1)
print("Cadastro efetuado.")
print()
sleep(1)

login =  input("Digite seu nome de usuario: ")
sleep(1)
pas= input("Digite a sua senha: ")

if login != user:
    print("print usuário incorreto!")
    login =  input("Digite seu nome de usuario: ")
    pas= input("Digite a sua senha: ")
if pas != password:
    print("Senha incorreta!")
    login =  input("Digite seu nome de usuario: ")
    pas= input("Digite a sua senha: ")
if login == user and pas == password:
    print()
    sleep(2)
    print("Seja bem vindo!")
    sleep(2)
    print("Vamos brincar? Tente adivinhar o numero de 0 a 10 que estou pensando! ")
    sleep(2)

continuar =True

numero= randint(0,10)
print(numero)

while continuar == True:
    jogar = int(input("Qual o seu palpite, de 0 a 10? "))
    print()
    if jogar == numero:
        print("Parabéns você acertou o número!")
        sleep(1)
        continuar = input("Você quer tentar novamente? [sim/não]")
        if continuar == "sim" or continuar == "SIM" or continuar =="s" or continuar == "S":
            continuar = True
        elif continuar == "não" or continuar == "NÃO" or continuar =="n" or continuar == "N":
            continuar == False
            print("Jogo finalizado!")
    elif jogar != numero:
        print("Você errou, mas não desanime! tente de novo.")
        sleep(1)
        continuar = input("Você quer tentar novamente? [sim/não]")
        if continuar == "sim" or continuar == "SIM" or continuar =="s" or continuar == "S":
            continuar = True
        elif continuar == "não" or continuar == "NÃO" or continuar =="n" or continuar == "N":
            continuar == False
            print("Jogo finalizado!")