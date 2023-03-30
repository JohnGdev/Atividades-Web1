"""1) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7 (h = altura)
c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso."""


if __name__ == "__main__":
    altura = float(input("Digite sua altura: "))
    sexo = input("Digite seu sexo (masculino ou feminino): ")
    
if sexo == "masculino":
    peso_ideal = (72.7 * altura) - 58
    #feminino
else:
    peso_ideal = (62.1 * altura) - 44.7
    
peso_atual = float(input("Digite seu peso atual em kg: "))

if peso_atual > peso_ideal:
    print("Você está acima do peso ideal.")
elif peso_atual < peso_ideal:
    print("Você está abaixo do peso ideal.")
else:
    print("Seu peso está dentro do peso ideal.")