# Em uma prova do Enem, em um dia, um aluno responde a uma avaliação de 90 perguntas de múltipla escolha com cada questão tendo respostas de A até E. Faça um algoritmo para ler as respostas de um aluno e o gabarito da prova, depois informe quantas questões ele acertou.

def gabarito_prova():
    import random

    gabarito = ["A","B","C","D","E"]
    random.shuffle(gabarito)
    respostas = []
    acertos = 0 
    nota = 0 # Nota vai de 0 a 100, a partir do acerto

    for i in range(5):
        respostas.append(input(f"Digite a resposta do aluno para a questão {i+1} (A, B, C, D ou E): ").upper())
        while respostas[i] not in ["A", "B", "C", "D", "E"]:
            print("Resposta inválida. Por favor, digite A, B, C, D ou E.")
            respostas[i] = input(f"Digite novamente a resposta do aluno para a questão {i+1} (A, B, C, D ou E): ").upper()

    for i in range(5):
        if respostas[i] == gabarito[i]:
            acertos += 1
            nota += (100 / 5)

    print("\n=== RESULTADO DA PROVA ===")
    print(f"\nO aluno acertou {acertos} questões.")
    print(f"A nota do aluno é: {nota:.2f}")

    print("\n=== RESPOSTAS DO ALUNO ===")
    print(respostas)

    print("\n=== GABARITO DA PROVA ===")
    print(gabarito)

# Ler um vetor A que conterá 15 números intiros; Contruir um vetor B do mesmo tipo, sendo que cada elemento do vetor B deverá ser a metade (parte inteira) de cada elemento de A.
def vetor_metade():
    A = []
    B = []

    for i in range(15):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        A.append(numero)
        B.append(numero // 2)

    print("\n=== VETOR A ===")
    print(A)

    print("\n=== VETOR B ===")
    print(B)


def menu():
    print("Escolha uma opção:")
    print("1. Gabarito da prova")
    print("2. Vetor metade")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")
    if escolha == '1':
        gabarito_prova()
    elif escolha == '2':
        vetor_metade()
    elif escolha == '3':
        print("Saindo do programa.")
    else:
        print("Opção inválida. Tente novamente.")

menu()