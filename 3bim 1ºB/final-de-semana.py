'''
Nome do programa: final-de-semana.py
Objetivo: Verifica se é final de semana ou não
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variável
dia = input("Que dia da semana é hoje? ").strip().lower()

# Verificador do dia da semana
if dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("É final de semana!!!")
else:
    print("É um dia útil")
