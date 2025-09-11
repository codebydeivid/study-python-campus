'''
Nome do programa: maioridade.py
Objetivo: Calcular a maioridade considerando o ano de nascimento
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

#Declaração de variáveis
from datetime import date
ano_nascimento = 0
ano_atual = date.today()
idade_atual = 0

#Recebimento de dados
ano_nascimento = input("Em que ano você nasceu? ")
idade_atual = int(ano_atual.year)-int(ano_nascimento)

print("Você atualmente tem", idade_atual, "hoje.")