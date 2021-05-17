
contatoslista =[('gustavo','1234-5678'), ("paulo", "9999-5461"), ("Jaque", "4321-2289"),  ("laura", "7894-3256")]
print(contatoslista[2][1])

teste =[("bruce", "123"),("ana", "9876")]
# para criar dicionarios utiliza-se {}
#para criar lista utiliza-se []


#contatos = {"gabriel":"1234-5678"}
#print(type(contatos))
#print(contatos) 


contatos = dict(contatoslista)
print(contatos)

print(contatos["Jaque"])
print(contatos["gustavo"])

teste2  = dict(teste)
print(teste2["bruce"])

#metodo get -> serve para bucas valor em dicionário

print(contatos.get("pedro", "contato não encontrado"))
print(contatos.get("Jaque", "contato não encontrado"))


# método values -> para buscar valor em um dicionário

print('1234-5678' in contatos.values())
print('1234-5652' in contatos.values())
print("-"*50)
contatos  ["mulher maravilha"] = "2233-9765"
contatos  ["deadpool"] = "2222-2222"
print(contatos)
print()
'''contatos [input("digite o nome: ")] = input("digite o telefone: ")
print(contatos)
print()'''

'''a = input("digite um nome:")
b = input("digite um telefone")
contatos [a]=b
print(contatos)'''

print("-"*100)
print("como deletrar contatos no dicionario")
del contatos["mulher maravilha"]
print(contatos)
print()
print(contatos.pop("gustavo"))
contatos.pop("Jaque")
print(contatos)
print()
#contatos.clear() #limpa tudo
print(contatos)
print("-"*100)
print("unindo dicionários")
print()

contatos_matheus =[('lucas','1234-7832'), ("carlos", "9999-2154"), ("arthur", "4321-5468"),  ("caio", "7894-3236")]
contatos3 = dict(contatos_matheus)
contatos4 = contatos.update(contatos3)
print(contatos)
