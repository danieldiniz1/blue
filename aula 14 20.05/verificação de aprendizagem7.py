from time import sleep
lista = []
listapares =[]
listaimpares= []
listafinal = []
while len(lista) <7:
    numero = int(input(f'digite um numero:'))
    lista.append(numero)
    sleep(1)

for nmrs in lista:
    if nmrs %2 ==0:
        listapares.append(nmrs)
    else:
        listaimpares.append(nmrs)

listapares.sort()
listaimpares.sort()
listafinal.extend(listapares)
listafinal.extend(listaimpares)

print(listafinal)
print()
for lista in listafinal:
    print(lista)
    sleep(1)


