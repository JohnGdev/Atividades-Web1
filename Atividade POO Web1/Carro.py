class Carro:
    
    def __init__(self, consumo):
        self.consumo = consumo
        self.autonomia = 0
        
    
    def andar(self, distancia):
        combustivel_gasto = distancia / self.consumo
        if combustivel_gasto <= self.autonomia:
            self.autonomia -= combustivel_gasto
            print(f"carro percorreu {distancia} km.")
        else:
            print("Não existe atonomia suficiente")
            
    def obterGasolina(self):
        return self.autonomia
    
    def adicionarGasolina(self, quantidade):
        self.autonomia += quantidade
        print(f"Abastecido com {quantidade} litros de gasolina. Nível atual: {self.autonomia} litros.") 
    
Ferrari = Carro(4)
Ferrari.adicionarGasolina(60)
Ferrari.andar(30)
print("Combustível restante:" + str (Ferrari.obterGasolina()) + "litros")
