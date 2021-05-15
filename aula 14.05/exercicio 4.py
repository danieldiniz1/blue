opc = 1

while opc ==1:
    palavra = input("digite uma palavra: ")
    
    while palavra != "gato":
        print("palavra incorreta")
        palavra = input("digite uma palavra: ")
    if palavra == "gato":
        opc = 0
        print("palavra correta ")
