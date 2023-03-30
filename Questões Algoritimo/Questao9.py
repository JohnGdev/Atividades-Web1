"""9) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

numeros = []

for i in range(10):
    numeros.append(float(input("Digite um número real: ")))

print("Vetor na ordem inversa:")
for numero in reversed(numeros):
    print(numero)
