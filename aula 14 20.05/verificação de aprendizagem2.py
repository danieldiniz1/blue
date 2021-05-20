frase = input('Digite uma frase: ')
vogais = 0
resposta = ""

for letra in frase:
    if letra in "aeiouAEIOU":
        vogais += 1
for letra in frase:
    if not letra in('aeiouAEIOU'):
        resposta += letra 
print("a frase sem as vogais é: ",resposta)
print('A frase tem %d vogais ' %(vogais))

