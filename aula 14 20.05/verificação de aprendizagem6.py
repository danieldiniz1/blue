lista = ["telefonou para a vitima? ", "Esteve no local do crime? ", "mora perto da vitima?", "devia para a vitima? ", "já trabalhou com a vitima ? "]


respostas = []
sim = 0


for lis in range (len(lista)):
    print(lista[lis])
    respostas.append(input("resposta: "))
    print()
for cont in respostas:
    if cont == "sim":
         sim += 1

if (sim <2):
    print("Você é inocente!")    
elif (sim ==2):
    print("Você é suspeito(a)")
elif (sim >=3 and sim <=4):
    print("Você é cumplice")
elif (sim ==5 ):
    print(" Você é o(a) assassino(a)!")
