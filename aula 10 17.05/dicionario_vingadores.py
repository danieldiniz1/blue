vingadores = {"Iron Man":"Robert Downey Junior", "Captain America": "Chris Evans", "Black Widow": "Scarlet Johansson ", "Thor": "Chris Hemsworth", "Hulk": "Mark Ruffallo", "Nick Furry": "Samuel L Jackson", "Vision":"Paul Bettany", "Antman": "Paul Rudd", "God": "Stan Lee" }
print()
print(vingadores)
print()
print(vingadores.get("Iron Man"))
print()
#for avengers in vingadores:
#   print(avengers)

for k,v in vingadores.items():
    print(f"{k} - {v}")