estoque = {
    "pão": [2000, 0.5],
    "salgado": [2000, 2.50],
    "pão de queijo": [4000, 0.30],
    "bolo": [0, 2]
    }
totalprodutos =0
totalvalor= 0 
continuar = True

while continuar == True:
    produto = input("Qual produto você quer comprar? ").lower()

    if produto in estoque:
        print("produto em estoque! ")
        print()
        qtd= int(input(f'quantos {produto} você quer comprar? '))
        print()
        if estoque[produto][0] < qtd:
        
         print("quantidade não disponivel para a compra")
        
        else: 
            print(f'você comprou {qtd} unidades de {produto} = R$ {(estoque[produto][1] * qtd):.2f}')
        
    estoque[produto][0]-=qtd
    totalprodutos+=qtd
    totalvalor+= (estoque[produto][1]*qtd)
        
    continuar = input('você quer continuar? [sim/não] ')
    if continuar == "sim" or continuar =="SIM":
        continuar = True
    elif continuar == "não" or continuar == "NÃO":
        continuar == False

print()
print(f'você comprou {totalprodutos} produtos, no total de R${totalvalor} reais')