def notas(n1,n2,n3):
    media = (n1+n2+n2)/3
    print(f'A média das 3 notas é: {media:.2f}')

def notas2(n1,n2,n3):
    maior1 = n1
    if n2 > maior1:
        maior1 = n2
    elif n3 > maior1:
        maior1 = n3
     
    maior2 = n1
    if n2 > maior2 and n2 <maior1:
        maior2 = n2
    elif n3 > maior2 and n3 <maior1:
        maior2= n3
   
    
    
    
    print(f'A média das 2 notas mais altas é: {(maior1+maior2)/2:.2f}')
    print(f'As maiores notas são: {maior1} e {maior2}')

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

notas(n1,n2,n3)
notas2(n1,n2,n3)

from datetime import date
def idade_votacao(AnoNascimento):
    DataAtual = date.today().year
    idade = DataAtual - AnoNascimento
    if (idade < 16):
        print(f'{idade} anos negado ')
    elif (idade <18 and idade >=16) or (idade>70):
        print(f'{idade} anos voto opcional')
    else:
        print(f'{idade} anos voto obrigatorio')
AnoNascimento = int(input("Digite sua data de nascimento: "))

idade_votacao(AnoNascimento)


def notas3(primeira,segunda,terceira):
    mediageral = (primeira+segunda+terceira)/3
    print(f"a média das 3 notas é: {mediageral}")

    if (primeira > segunda and primeira > terceira) and (segunda >= terceira):
        print(f'a média das duas notas mais altas é: {(primeira+segunda)/2:.2f}')
    elif (terceira >=segunda):
        print(f'a média das duas notas mais altas é: {(primeira+terceira)/2:.2f}')
    if (segunda > primeira and segunda > terceira) and (terceira > primeira):
        print(f'a média das duas notas mais altas é: {(segunda+terceira)/2:.2f}')

    maiornota = primeira
    if (segunda > maiornota):
        maiornota = segunda
    if (terceira > maiornota):
        maiornota = terceira
    print(f"a maior nota é: {maiornota} ")
    menornota = primeira
    if (segunda < menornota):
        menornota = segunda
    if (terceira < menornota):
        menornota = terceira
    print(f'a menor nota é: {menornota}')

primeiranota = float(input("digite a primeira nota: "))
segundanota = float(input("digite a segunda nota: "))
terceiranota = float(input('digite a terceira nota: '))

notas3(primeiranota,segundanota,terceiranota)