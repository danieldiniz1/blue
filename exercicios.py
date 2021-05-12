def soma (a,b,c):
    print("a somas dos números é: ", a+b+c)

n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))
n3 = int(input("digite o terceiro número: "))

soma(n1,n2,n3)
print()

#sabendo se é p ou n

def pn (x):
    if x > 0:
        print("P")
    elif x < 0:
        print("N")
    else:
        print('0')
x = int(input("digite o número: "))
pn(x)

print()
def SomaIposto(taxa,custo):
    custo = custo + (custo * taxa /100 )
    return custo
taxa = float(input("Insira o valor da taxa: "))
custo = float(input("Digite o valor de custo: "))

custo = SomaIposto(taxa,custo)

print(f"O preço com impostos é: {custo:.2f}")
print()   

horas = float(input("Insira a quantidade de horas trabalhadas: "))
salario = 15

if horas > 40:
    salario = 16.5
print("O salario é: ", horas * salario)    
print()

def sl (horas,valor):
    if horas > 40:
        vlr = 16.5
        print("o salario é: ", hrs * vlr )
    else:
        vlr= 15
        print("o salario é: ", hrs * vlr)

hrs = float(input("Digite a quantidade de horas trabalhadas: "))
vlr = 15

sl(hrs,vlr)

print()
# imc
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print(f'seu imc é: {peso / (altura * altura):.2f}')

print()
# nota
def nota (a):
    if a >= 9:
        print("você tirou A ")
    elif a >= 8:
        print("Você tirou B ")
    elif a >= 7:
        print("você tirou C ")
    elif a >= 6:
        print("você tirou D ")
    elif a <= 5:
        print("você tirou F ")

nt = float(input("digite a nota: "))

nota(nt)

print()

def menor (c,x):
    if c < x:
        print(c, "é o menor numero")
    elif x < c:
        print(x, "é o menor numero")
    elif c == x:
        print("os dois numeros são iguais")
mr1 = float(input("digite o 1 numero: "))
mr2 = float(input("digite o 2 numero: "))

menor(mr1,mr2)