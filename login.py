'''
Nome do programa: login.py
Objetivo: Login com usuário e senha definido
Autor: Deivid Henrique
Data: 17/04/2025
Versão: 1.0
'''

# Declaração de variáveis
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar se login e senha estão corretos
if login == "admin" and senha == "1234":
    print("Usuário autorizado")
else:
    print("Usuário e senha não encontrados")
