'''
Nome do programa: aposentadoria.py
Objetivo: Verifica se você está apto a se aposentar
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
sexo = input("Qual seu sexo (masculino/feminino)? ").lower()
idade = int(input("Quantos anos tem? "))
tempo_contrib = int(input("Informe seu tempo de contribuição (em anos): "))

# Verificação se está apto a aposentadoria
if (sexo == "feminino" and idade >= 60 and tempo_contrib >= 30) or (sexo == "masculino" and idade >= 65 and tempo_contrib >= 35):
    print("Você já pode se aposentar")
else:
    print("Você ainda não pode se aposentar")
