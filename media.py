'''
Nome do programa: media.py
Objetivo: Calcular a media do aluno de acordo com suas notas bimestrais
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
nota_bim1 = int(input("Digite a nota do primeiro bimestre: "))
nota_bim2 = int(input("Digite a nota do segundo bimestre: "))
nota_bim3 = int(input("Digite a nota do terceiro bimestre: "))
nota_bim4 = int(input("Digite a nota do quarto bimestre: "))

# Calcula a média
media = (nota_bim1 + nota_bim2 + nota_bim3 + nota_bim4) / 4

# Verificação de aprovação
if media >= 60:
    print("Parabéns, você foi aprovado, sua média anual é", media)
else:
    print("Você não foi aprovado, sua média é", media)