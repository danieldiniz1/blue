lista = ["telefonou para a vitima? ", "Esteve no local do crime? ", "mora perto da vitima?", "devia para a vitima? ", "já trabalhou com a vitima ? "]


respostas = []
sim = 0


for lis in range (len(lista)):
    print(lista[lis])
    respostas.append(input())
    print()
for cont in respostas:
    if cont == "sim":
         sim += 1
if (sim <2):
    print("inocente")    
elif (sim ==2):
    print("suspeito")
elif (sim >=3 and sim <=4):
    print("cumplice")
elif (sim ==5 ):
    print("assassino")



#
precopao = float(input("digite o preço do pão"))

for cont in range(1,51):
    print("quantidade-R$",(cont,precopao*cont))
    print()






