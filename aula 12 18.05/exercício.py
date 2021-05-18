#exercícios 1 e 2

lista_quadrados = [1, 4, 5, 6, 7, 9 ]

dicionario_quadrados = {}

lista_inteiros = {}

for numeros in lista_quadrados:
    dicionario_quadrados.update({numeros: numeros**2})

print("dicionario quadrado 1")
print(dicionario_quadrados)
print("-"*150)
for numero in  range(1,11):

    lista_inteiros.update({numero: numero**2})
print("dicionario quadrado 2")
print(lista_inteiros)