
opc = True

gabriel = 0
pedro = 0
matheus = 0
ana = 0
nulo = 0
branco = 0
total = 0

while opc ==True :
    print("eleição! numero dos candidatos: 1- gabriel, 2- pedro, 3- matheus, 4- ana, 5- NULO, 6- BRANCO.")
    voto = int(input("Digite seu voto: "))

    if voto == 1 :
        gabriel += 1
        total += 1

    elif voto == 2 :

        pedro += 1

        total +=  1

    elif voto == 3 :

        matheus += 1

        total += 1

    elif voto == 4 :

        ana +=1

        total +=1

    elif voto == 5 :

        nulo +=1

        total +=1

    elif voto == 6 :

        branco +=1

        total +=1

    elif voto ==0:
        opc = False

print("Total de votos:", total)
print(f"Total de votos do candidato gabriel: {gabriel} votos / {((gabriel/total)*100):.2f}  %")
print(f"Total de votos do candidato pedro: {pedro} votos / {((pedro/total)*100):.2f}  %")
print(f"Total de votos do candidato matheus: {matheus} votos / {((matheus/total)*100):.2f}  %")
print(f"Total de votos do candidata ana: {ana} votos / {((ana/total)*100):.2f}  %")
print("Total de votos nulos: ", nulo)
print("Total de votos brancos: ", branco)
print(f"Percentual de votos nulos pelo total:  {((nulo/total)*100):.2f}  %")
print(f"Percentual de votos brancos pelo total: {((branco/total)*100):.2f}  %")