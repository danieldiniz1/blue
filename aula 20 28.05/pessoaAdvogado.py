from pessoa import Pessoa


class PessoaAdvogado(Pessoa): #Herança

    #construtor de atributos 

    def __init__(self,oab, nome, idade, cpf, telefone, ):
        self.__oab = oab       
        super().__init__(nome, idade, cpf, telefone)

#get
    def getOab(self):
        return self.__oab

#set
    def setOab(self, oab):
        self.__oab = oab


