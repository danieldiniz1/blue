

# custo total da viagem
def Custoviagem(noites,cidade,diasaluguel,gastoextra):

   
    ValorPorNoite = 140
    ValorHospedagem = noites * ValorPorNoite
    print(f'O valor total de hospedagem é: R${ValorHospedagem:.2f}')

    
    cidade = cidade.lower() .strip()
    ValorCidade = 0

    if (cidade == "são paulo") or (cidade == "sao paulo"):
        ValorCidade = 312
    elif (cidade == "porto alegre"):
        ValorCidade = 447
    elif (cidade == "recife"):
        ValorCidade = 831
    elif (cidade == "manaus"):
        ValorCidade = 986

    print(f'O custo da passagem é: {ValorCidade:.2f}')

   
    ValorDia = 40
    Desconto7dias = 50
    Desconto3dias = 20

    CustoCarro = ValorDia * DiasAluguel

    if (DiasAluguel >= 7):
        CustoCarro -= Desconto7dias
    elif (DiasAluguel >= 3):
        CustoCarro -= Desconto3dias
    print(f'O aluguel do carro custa: R${CustoCarro:.2f}')

    print('O gasto extra é: R${gastoextra:.2f}')



noites = int(input("Quantas noites de hospedagem? "))
cidade = input("Qual é a cidade de destino? ")
DiasAluguel = int(input("Por quantos dias você quer alugar o carro? "))
gastoextra = float(input("Digite o valor do gasto extra"))

print()
Custoviagem(noites,cidade,DiasAluguel,gastoextra)