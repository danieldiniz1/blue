def gasto(tabaco,seda,filtro,semana):
    custototal = (tabaco + seda + filtro) * semana
    print(f"o gasto semanal com tabaco é: R${tabaco+seda+filtro:.2f}")
    print()
    print(f'o gasto mensal com tabaco é: R${custototal:.2f}')

tabaco = float(input("Digite o preço do tabaco: "))
print()
seda = float(input("Digite o preço da seda: "))
print()
filtro = float(input("Digite o preço do filtro: "))
print()
semana = int(input("quantas semanas: "))
print()

gasto(tabaco,seda,filtro,semana)
print()

exit = input("digite algo para sair")
