def notas(primeira,segunda,terceira):

    mediageral = (primeira + segunda + terceira)/3
    print(f'A média das 3 notas é: {mediageral:.2f}')

    if (primeira > segunda and primeira > terceira ) and (segunda > terceira):
        print(f"A média das maiores notas é: {(primeira+segunda)/2:.2f}")
    elif (terceira >= segunda):
        print(f'A média das maiores notas é: {(primeira+terceira)/2:.2f}')
    if (segunda > primeira and segunda > terceira) and (terceira > primeira):
        print(f'A média das maiores notas é: {(segunda+terceira)/2:.2f}')


    maior = primeira

    if (segunda > maior):
        maior = segunda
    elif (terceira > maior):
        maior = terceira
    print(f"A maior nota é: {maior}")


    menor =  primeira
    if (segunda < menor):
        menor = segunda
    elif (terceira < menor ):
        menor = terceira
    print(f"a menor nota é: {menor}")

primeira = float(input("digte a primeira nota: "))
segunda = float(input("digite a segunda nota: "))
terceira = float(input("digite a terceira nota: "))

notas(primeira,segunda,terceira)
print()

exit = input("digite algo para sair")



    