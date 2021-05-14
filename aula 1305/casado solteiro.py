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

for cont in range(10,0,-1):
    print(cont)
    print()


frase = "Go blue, "
print(10*frase)

for cont in range(1,11):
    print("Go blue")
    print()


for cont in range(-0,21,2):
    print(cont)
    print()

