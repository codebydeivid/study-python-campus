'''
Nome do programa: semaforo.py
Objetivo: Um semaforo que mostra o que é preciso fazer de acordo com a cor
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
cor = int(input("Qual a cor da sinaleira (1 para vermelho, 2 para verde)? "))

# Avisos do semáforo
if cor == 1:
    print("PARE")
elif cor == 2:
    print("SIGA")
else:
    print("Opção inválida")