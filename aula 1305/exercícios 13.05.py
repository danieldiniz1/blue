#exercício 1
tb = int(input("digite a tabuada que você quer ver: "))
for cont in range(0,11):
    print(tb*cont)
    print()


# exercício 2
for cont in range(10,0,-1):
    print(cont)
    print()

# exercício 3
casado = 0
solteiro = 0

for situacao in range(0,15):
    situacao = input("Digite seu estado civil atual: ")
  
    if situacao == "casado":
        casado +=1
    elif situacao == "solteiro":
        solteiro +=1
    else:
        print("entrada invalida")
print("a lista tem %d casados  %d solteiros" %(casado,solteiro))
print()

# exercício 4

for cont in range(1,11):
    print("Go blue")
    print()

# exercício 5

for cont in range(1,21,2):
    print(cont)
    print()

# exercício 6

precopao = float(input("digite o preço do pão"))

for cont in range(1,51):
    print("quantidade-R$",(cont,precopao*cont))
    print()

#exercício 8

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



# desafio 1
for i in range(1000,10000):
  parte1 = i // 100
  parte2 = i % 100
  if (parte1+parte2)**2 == i:
    print(i)




# desafio 2 
materias = int(input("quantas materias existem?"))   
notas = []

for cont in range(materias):
    nota = float(input(f"qual nota você tirou na {cont+1} materia? "))
    notas.append(nota)
print('a média geal das notas é: ')
print(sum(notas)/materias)
    