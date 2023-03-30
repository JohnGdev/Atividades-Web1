class Matriz:
    dic = None
    tamanho = None
    
    
    def __init__(self):
        self.dic = {}
        self.tamanho = 0
        
    def __init__(self, matriz, tamanho):
        self.dic = matriz
        self.tamanho = tamanho
        
    def imprimeMatriz(self):
        for i in range(self.tamanho):
            stLinha = ""
            for j in range(self.tamanho):
                stLinha += self.dic[(i,j)] + " " 
            print(stLinha)