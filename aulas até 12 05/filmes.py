filmes = ["Os vingadores", "Harry Potter", "Forrest Gump", "A procura da felicidade", "Como eu era antes de você", "O lobo de wall street", "Dois coelhos", "Up", "Lagoa azul"]
print(filmes)
print()
filmes.append("homem de ferro")
print()
print(filmes)
print()
filmes_novos = ["historias cruzadas", "esqueceram de mim", "desventuras em serie", "poderoso chefão", "De volta para o futuro", "ben hur"]

filmes.extend(filmes_novos)
print(filmes)
print()
filmes.sort()
print(filmes)
#filmes.reverse()
#print(filmes)
print()
print()



filmes.insert(0, "Pianista")
filmes.insert(10, "Projeto x")
filmes.sort()
print(filmes)
print()
#filmes.remove("Harry Potter")
#print(filmes)
#print()
#filmes.remove("A procura da felicidade")
#print(filmes)
#print()
#filmes.pop(0)
#filmes.pop()
#del filmes[1]
#del filmes[2:6]
print("Harry Potter" in filmes)
for filme in filmes:
    print(filme)
print(len(filmes))