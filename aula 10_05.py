print ("funções")
print()
# definindo uma função 

def blue():
    print("eu sou um blummer")

#chamando a função
blue()

print()
print("exemplo de função com parâmetros")
print()
#definindo a função:
def subtracao (a,b): # a e b são parâmetros da minha fução
    print("a subtração é:", a-b)

def soma (c,d):      
    print("a soma é: ",c+d)

def multiplicacao (e,f): 
    print("a multiplicação é: ", e*f)

def div (a,b):
    print(f"a divisão é: {a/b:.2f}")

#chamando a função
subtracao (10,5)
print()
soma (10,5)
print()
multiplicacao (48,20)
print()
div (40,6)
print()