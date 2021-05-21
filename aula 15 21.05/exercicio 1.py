numeros = []
for nm in range(5):
    numero = int(input(f"Digite o {nm+1}º número: "))
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)
print("Lista: ", numeros)
for nmrs in numeros:
    print(nmrs)