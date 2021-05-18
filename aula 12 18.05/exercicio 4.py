from random import randint
from operator import itemgetter


jogados = {}

for jogadores in range(1,5):
    print()
    nomejogador = input("quem esta jogando? ")
    print()
    jogar = input("digite jogar: ")

    while jogar != "jogar":
        print()
        print("você não jogou tente novamente")
        jogar =input("digite jogar: ")
        

    if jogar == "jogar":
        dado = randint(1,6)
        jogados.update({nomejogador:dado})
print()
print("-"*25)
print("numeros tirados pelos jogadores no dado: ")
for i in sorted(jogados, key= jogados.get, reverse=True):
    print(i, jogados[i])
print("-"*25)
print("Ranking dos jogadores: ")
for k,v in enumerate(sorted(jogados, key=jogados.get, reverse=True)):
    print(f'{k+1}º Lugar: {v}')
print()

