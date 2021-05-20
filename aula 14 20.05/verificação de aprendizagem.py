#exercício 1

nmr1 = float(input("digite o primeiro numero: "))
nmr2 = float(input("digite o segundo numero: "))

print(f'A soma dos numeros é: {(nmr1+nmr2):.2f}')
print(f"A multiplicação dos dois numeros é: {(nmr1*nmr2):.2f}")
print(f"A divisão dos numeros é: {(nmr1//nmr2):.2f}")
maior = nmr1
if nmr2> maior:
    print(f"o numero {nmr2} é o maior")
else:
    print(f"o numero maior é o {nmr1}")

if ((nmr1+nmr2)%2)==0:
    print("a soma dos numeros é par")
else:
    print("a soma dos numeros é impar")

if (nmr1*nmr2)>40:
    print((nmr1*nmr2) / (nmr1//nmr2))
else:
    print("a multiplicação não foi maior que 40")


# exercício 2



