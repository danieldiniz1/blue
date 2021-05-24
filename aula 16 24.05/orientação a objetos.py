# classe -> molde para criar os nossos objetos
# objetos -> instâncias da classe (parte funcional da classe)
# atributos -> características dos objetos 
# metodos -> ações que os objetos executam

# classe: herói 
# objeto: capitão américa 
# atributos: nome, idade, peso, altura 
# metodos: engordar


class Herói():
    def __init__(self,nome,idade,peso,altura,sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    def engordar(self,peso):
        self.peso += peso

    def envelhecer(self, idade):
        self.idade += idade

if (__name__ == "__main__"):
    heroi = Herói("Capitão América", 30, 85, 1.90, "masculino")
print(vars(heroi))
heroi.engordar(int(input("Digite quantos Kg você engordou: ")))
print(vars(heroi))
print()
if heroi.peso >90:
    print("Acima do peso")
print(f'Nome: {heroi.nome}')
print(f"{heroi.idade} anos.")
print(f'{heroi.peso} KG')
print(f'Altura: {heroi.altura:.2f}')
print(f'Sexo: {heroi.sexo}')
print()
heroi.envelhecer(int(input("Digite quantos anos a mais: ")))
atributos = dict(vars(heroi))
for atributo in atributos:
    print(atributos[atributo])