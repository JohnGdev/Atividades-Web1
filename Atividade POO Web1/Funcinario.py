class Funcionario:
    
    def __init__(self, nome, salario = 0):
        self.nome = nome
        self.salario = salario
        
    def aumentarSalario (self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento
        
funcionario = Funcionario("John", 25000)


print("Salário atual de", funcionario.nome, ":", funcionario.salario)


funcionario.aumentarSalario(10)

print("Salário atualizado de", funcionario.nome, ":", funcionario.salario)
        
        