vingadores = {"Iron Man":"Robert Downey Junior", "Captain America": "Chris Evans", "Black Widow": "Scarlet Johansson ", "Thor": "Chris Hemsworth", "Hulk": "Mark Ruffallo", "Nick Furry": "Samuel L Jackson", "Vision":"Paul Bettany", "Antman": "Paul Rudd", "God": "Stan Lee" }
print()

vingadores_lista = ["Miranha", "Lóqui", "Tãnuz", "Bátima"]


print(vingadores)
print()
print(vingadores.get("Iron Man"))
print()
#for avengers in vingadores:
#   print(avengers)

'''for k,v in vingadores.items():
    print(f"{k} - {v}")'''

for i,v in enumerate (vingadores_lista):
        print(i+1,v)