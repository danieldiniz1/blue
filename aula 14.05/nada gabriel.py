
nomeidade = []
cont = 0
while cont <5:
    for lis in nomeidade:
        nome = input("digite seu nome: ")
        idade = int(input("digite sua idade: "))
        nomeidade.append(nome)
        nomeidade.append(idade)
        cont +=1
        print()
print(nomeidade)