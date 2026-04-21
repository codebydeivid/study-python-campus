'''
Nome do programa: triangulo.py
Objetivo: Mostrar o tipo do triangulo baseado na medida dos lados recebidos
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))

# Verificação do tipo de triângulo
if lado1 == lado2 == lado3:
    print("Seu triângulo é Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Seu triângulo é Isósceles")
else:
    print("Seu triângulo é Escaleno")
