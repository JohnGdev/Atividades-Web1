class Livro:
    
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setPreco(self, value):
        self.preco = value
        
l1 = Livro('Pai rico e pai pobre', 200, 'John', 150)
print(l1.getPreco())
l1.setPreco(300)
print(l1.getPreco())

print(" Livro: " + l1.nome + "\n Autor: " + l1.autor + "\n numero de paginas: " + str (l1.qtdPaginas) + "\n Preço: " + str (l1.getPreco()))

l1.setPreco(400)

print(" Livro: " + l1.nome + "\n Autor: " + l1.autor + "\n numero de paginas: " + str (l1.qtdPaginas) + "\n Preço: " + str (l1.getPreco()))

