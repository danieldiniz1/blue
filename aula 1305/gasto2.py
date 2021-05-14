def gasto2(agua,luz,telefone,tv,comida):
    custosemana = (agua+luz+telefone+tv+comida) / 4 
    customes = (agua+luz+telefone+tv+comida)
    custoano = (agua+luz+telefone+tv+comida) * 12 
    print(f"o custo de vida por semana é: R${custosemana:.2f}")
    print()
    print(f'o custo de vida por mês é: R${customes:.2f}')
    print()
    print(f'o custo de vida por ano é: R${custoano:.2f}')
    print()

agua = float(input("digite o gasto com água por mês: "))
print()
luz = float(input("digite o gasto de luz por mês: "))
print()
telefone = float(input("digite o gasto com telefone por mês: "))
print()
tv = float(input("digite o gasto com tv a cabo por mês: "))
print()
comida = float(input("digite o gasto com comida por mês: "))
print()
gasto2(agua,luz,telefone,tv,comida)
print()

exit = input("digite algo para sair ")
