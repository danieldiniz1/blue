tb = int(input("digite a tabuada que você quer ver: "))
for cont in range(0,11):
    print(tb*cont)
    print()



materias = int(input("quantas materias existem?"))   
notas = []

for cont in range(materias):
    nota = float(input(f"qual nota você tirou na {cont+1} materia? "))
    notas.append(nota)
 
print(sum(notas)/materias)
    