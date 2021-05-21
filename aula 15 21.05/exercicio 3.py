frase = input('Informe uma frase: ').split(" ")  # retira espaço em branco
aux = ""

for i in range(0, len(frase)):
    aux += frase[i]

frase = aux.split(".") #retira os pontos
aux = ""

for i in range(0, len(frase)): #retira os pontos
    aux += frase[i]

frase = aux.split(",") #retira as vírgulas
aux = ""

for i in range(0, len(frase)): #retira as vírgulas
    aux += frase[i]

if aux.lower() == aux.lower()[::-1]: #verifica usando minúsculo e invertido
    print ('É palíndromo')
else:
    print ('Não é palíndromo')