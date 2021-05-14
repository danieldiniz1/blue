def custohospedagem(noites):
    valorpornoite = 140
    valorhospedagem = noites* valorpornoite
    print(f'o custo total de hospedagem é: R${valorhospedagem:.2f}')
noite = int(input("Quantas noites de hospedagem? "))
custohospedagem(noite)
print()


def passagem(cidade):
    cidade.lower().strip()
    precocidade = 0
    if (cidade == "são paulo") or (cidade == "sao paulo"):
        precocidade = 312
    elif (cidade == "porto alegre"):
        precocidade = 447
    elif (cidade == "recife"):
        precocidade = 831
    elif (cidade == "manaus"):
        precocidade = 986
    
    print(f"o custo da passagem é: R${precocidade:.2f}")
print("Cidades disponíveis: São paulo, Porto Alegre, Recife, Manaus.")
cidade = input("Qual a cidade de destino? ")
passagem(cidade)

def aluguelcarro(diasaluguel):
    valordia = 40
    descontosetedias = 50
    descontotreisdias = 20

    custocarro = valordia * diasaluguel

    if (diasaluguel >=7):
        custocarro -= descontosetedias
    elif (diasaluguel >=3):
        custocarro -= descontotreisdias

    print(f'o custo do aluguel do carro é: R$ {custocarro:.2f}')

diasaluguel = int(input("quantos dias de aluguel do carro? "))
aluguelcarro(diasaluguel)
print()

def custoviagem(noites,cidade,diasaluguel,taxaextra):

            valorpornoite = 140
            valorhospedagem = noites * valorpornoite
            print(f'o custo total de hospedagem é: R${valorhospedagem:.2f}')
            print()


            cidade.lower().strip()
            precocidade = 0
            
            if (cidade == "são paulo") or (cidade == "sao paulo"):
                precocidade = 312
            elif (cidade == "porto alegre"):
                precocidade = 447
            elif (cidade == "recife"):
                precocidade = 831
            elif (cidade == "manaus"):
                precocidade = 986
    
            print(f"o custo da passagem é: R${precocidade:.2f}")
            print()


            valordia = 40
            descontosetedias = 50
            descontotreisdias = 20

            custocarro = valordia * diasaluguel

            if (diasaluguel >=7):
                custocarro -= descontosetedias
            elif (diasaluguel >=3):
                custocarro -= descontotreisdias

            print(f'o custo do aluguel do carro é: R${custocarro:.2f}')
            print()

    
            print(f"o total do gasto extra é: R${taxaextra:.2f}")
            print()

            custototal = (valorhospedagem + precocidade + custocarro + taxaextra)

            print()
            print(f'o custo total é: R${custototal:.2f} Boa viagem! :D')

noites = int(input("Quantas noites hospedado? "))
cidade = input("Qual a cidade de destino? ")
diasaluguel = int(input("Quantos dias de aluguel do carro? "))
taxaextra = float(input("Qual o valor do gasto extra? "))
print()


custoviagem(noites,cidade,diasaluguel,taxaextra)
print()


from datetime import date 
def idadevotacao (anonascimento):

        dataatual =date.today().year
        idade = dataatual - anonascimento

        if (idade < 16):
            print(f"{idade} anos voto negado!")
        elif (idade >= 16 and idade < 18):
            print(f'{idade} anos voto opcional!')
        else:
            print(f'{idade} anos voto obrigatorio!')

anonascimento = int(input("digite seu ano de nascimento: "))
idadevotacao(anonascimento)
print()
    
    






a = input("digite algo")