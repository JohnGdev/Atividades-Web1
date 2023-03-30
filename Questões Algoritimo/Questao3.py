"""3) Faça um Programa que leia três números e mostre-os em ordem decrescente."""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os três números
lista_numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
lista_numeros.sort(reverse=True)

# Exibe a lista em ordem decrescente
print("Os números em ordem decrescente são: ", lista_numeros)
