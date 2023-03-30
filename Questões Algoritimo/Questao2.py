"""2) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos)."""

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))

velocidade_internet = float(input("Digite a velocidade do link de internet em Mbps: "))

tempo_download = (tamanho_arquivo * 8) / velocidade_internet / 60


print("O tempo aproximado de download é de " + str(round(tempo_download, 2)) + " minutos.")

