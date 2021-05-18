# exercício 5

from datetime import date

dados = {}


for informacoes in range(1):
    nome = input("qual o seu nome? : ")
    dados.update({"nome":nome})   
    nascimento = int(input("Qual o seu ano  de nascimento? : "))
    idade = (2021 - nascimento)
    dados.update({"idade":idade})
    ctps = int(input("qual a sua carteira de trabalho? (0 não tem): "))
    if ctps == 0:
        dados.update({"Carteira de trabalho Nº":"não tem!"})
    else:
        dados.update({"carteira de trabalho Nº":ctps})
        contratacao = int(input("Digite o ano em que foi contratado: "))
        dados.update({"Ano de contratação":contratacao})
        salario = float(input("Digite o valor do salário: "))
        dados.update({"Salário em R$":salario})
        aposentadoria = (35 - (2021-contratacao))
        dados.update({"Quantos anos de trabalho faltam para se aposentar ":aposentadoria})
        a_receber = ((aposentadoria*12)*salario)
        dados.update({"Você vai receber até se aposentar: ":a_receber})


print()
for informacoes in dados:
    print(f'{informacoes}: {dados[informacoes]}')