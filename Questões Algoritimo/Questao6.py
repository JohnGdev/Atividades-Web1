"""6) Faça um programa que leia 5 números e informe o maior número."""


numero1 = float(input("digite um numero: "))
numero2 = float(input("digite um numero: "))
numero3 = float(input("digite um numero: "))
numero4 = float(input("digite um numero: "))
numero5 = float(input("digite um numero: "))

numeros = [numero1, numero2, numero3, numero4, numero5]

print("O maior número é:", max(numeros))