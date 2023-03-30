class Triangulo:
    
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    def calcular(self):
        return self.ladoA + self.ladoB + self.ladoC
        
    
    def qual_maior_lado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print ("Lado A é maior")
        elif self.ladoB > self.ladoC:
            print ("Lado B é maior")
        else:
            print ("Lado C é maior")


ladoA = float(input("Digite o comprimento do lado A: "))
ladoB = float(input("Digite o comprimento do lado B: "))
ladoC = float(input("Digite o comprimento do lado C: "))

            
triangulo = Triangulo(ladoA, ladoB, ladoC)

print ("o perimetro do triangulo é: ", triangulo.calcular())
triangulo.qual_maior_lado()


        
        
