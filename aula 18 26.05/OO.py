class funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.__valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property
    def salario (self):
            return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("impossivel alterar salário diretamente. utilize a função calcula_salario().")

    def registra_horas_trabalhadas(self, horas_trabalhadas):
        self.__horas_trabalhadas = horas_trabalhadas
    
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.__valor_hora_trabalhada

matheus = funcionario("matheus", "dev junior", 50)
matheus.registra_horas_trabalhadas(15)
matheus.calcula_salario()
print(matheus.salario)
matheus.__salario = 5000
print(matheus.salario)
print(matheus.__salario)
print(type(matheus))
print(type(vars(matheus)))