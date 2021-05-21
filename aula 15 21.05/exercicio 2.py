numeros = []

for nmrs in range(10):
    numero = int(input(f"digite o {nmrs+1}º número: "))
    numeros.append(numero)
    numeros.sort()
    numeros.reverse()

print()
print(f"tamanho da lista:",len(numeros))
if 5 in numeros:
    print("A número 5 está na lista ")
else:
    print("O número 5 não está na lista.")
for n in numeros:
    print(n)