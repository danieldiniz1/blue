from telefone import Telefone

class Pessoa():
    #construtor de atributos 
    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf 
        self.__telefone = Telefone(telefone)

# Get 

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getCpf(self):
        return self.__cpf
    
    def getTelefone(self):
        return self.__telefone

# Set

    def setNome(self, nome):
        self.__nome = nome
    
    def setIdade(self, idade):
        self.__idade = idade
    
    def setCpf(self, cpf):
        self.__cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone().setTelefone(telefone)
