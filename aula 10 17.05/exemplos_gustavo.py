perguntas = ["nome", "idade", "sexo"]
respostas = ["Buce Lee", "81", "masculino" ]

perguntas2 = dict(perguntas)
respostas2 = dict(respostas)

for p,r in zip(perguntas,respostas):
    print(f'Qual seu/sua {p}? é {r}')