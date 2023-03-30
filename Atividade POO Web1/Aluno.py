class Aluno:
    
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
        
    def estudar(self,value):
        self.tempoSemDormir += value
        
    def dormir(self,value):
        self.tempoSemDormir -= value
        
a1 = Aluno('John', 'ADS', 12)

a1.dormir(8)
a1.estudar(4)

print(a1.tempoSemDormir)