frase = "vai curinthians (contra a minha vontade)"
for letra in frase:
    print(letra,end=" ")


for cont in range(0,4):
            print(cont)

print()

for cont in range(0,12,2):
    print(cont) 
print()

for cont in range(10,-1,-1):
    print(cont)

print()

for cont in range(0,20,2):
    print(cont)


texto = input("digite uma frase ")
vogais = 0
espacos = 0

for letra in texto:
    if letra == " ":
        espacos += 1
    elif letra in "aeiou":
        vogais += 1

print("a frase tem %d vogais e %e espaços." %(vogais,espacos))





print()
exit = input("digite algo para sair ")
