# exercício 3

quantidadealunos = int(input("digite quantos alunos existem na turma: "))

nome_media ={}
nome_situacao ={}

while len(nome_media) != quantidadealunos:
    nome = input("digite seu nome: ")
    media = float(input("digite a media das notas: "))
    nome_media.update({nome:media})



    if media >= 7:
        nome_situacao.update({nome:"aprovado"})
    elif media >=5 and media <=6.9:
        nome_situacao.update({nome:"recuperação"})
    else:
        nome_situacao.update({nome:"reprovado"})
print()
print(nome_media)
print()
print(nome_situacao)