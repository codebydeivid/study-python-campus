'''
Nome do programa: termometro.py
Objetivo: Mostra o que a pessoa (hiportemia, normal, febre ou febre alta) de acordo com a temperatura mostrada
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
temperatura = float(input("Qual a temperatura corporal? "))

# Verifica o estado da pessoa a partir da temperatura 
if temperatura < 35:
    print("Hipotermia")
elif 35 <= temperatura <= 37.5:
    print("Temperatura normal")
elif 37.6 <= temperatura <= 39:
    print("Febre")
else:
    print("Febre alta")