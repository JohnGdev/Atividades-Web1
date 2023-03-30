class pessoa:
    nome = None
    idade = None
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def getAnoNascimento(self, anoAtual):
        return anoAtual - self.idade
    
pessoa = pessoa ("John",25)
print(pessoa.getAnoNascimento(2023))
    