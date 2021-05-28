from pessoa import Pessoa

class PessoaMedico(Pessoa):
    def __init__(self, crm,  nome, idade, cpf, telefone):
        self.__crm = crm
        super().__init__(nome, idade, cpf, telefone)

#get
    def getCrm(self):
        return self.__crm

#set
    def setCrm(self, crm):
        self.__crm = crm
