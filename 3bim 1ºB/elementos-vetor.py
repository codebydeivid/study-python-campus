# Ler um vetor A com 20 elementos negativos. Construir um vetor V com os mesmos elementos do vetor A,
# porém com seus valores positivos.
def negativos_para_positivos():
    A = []
    V = []
    Q = 20

    for i in range(Q):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número negativo: "))
                if num >= 0:
                    print("Número inválido. Por favor, digite um número negativo.")
                    continue
                A.append(num)
                V.append(-num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro negativo.")

    print(f"Vetor A: {A}")
    print(f"Vetor V: {V}")

# Altere o exercício anterior para realizar a operação escolhida pelo usuário da seguinte: a operação do primeiro
# valor do vetor pelo último valor do segundo vetor, o segundo valor do primeiro vetor pelo
# penúltimo do segundo vetor. O resultado deve ser armazenado em um terceiro vetor na
# primeira posição, segunda, e assim por diante. 
def produto_cruzado():
    A = []
    B = []
    C = []
    Q = 20

    def bonito(texto):
        print("\n")
        print("-" * 40)
        print(texto)
        print("-" * 40)

    bonito("Primeira lista de números:")
    for i in range(Q):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número: "))
                A.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

    bonito("Segunda lista de números:")
    for i in range(Q):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número: "))
                B.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

    for i in range(Q):
        Op = input(f"Digite a operação para A[{i}] e B[{Q - 1 - i}] (+, -, *, /): ")
        if Op == '+':
            C.append(A[i] + B[Q - 1 - i])
        elif Op == '-':
            C.append(A[i] - B[Q - 1 - i])
        elif Op == '*':
            C.append(A[i] * B[Q - 1 - i])
        elif Op == '/':
            if B[Q - 1 - i] != 0:
                C.append(A[i] / B[Q - 1 - i])
            else:
                C.append(None)
        else:
            print("Operação inválida. Armazenando None.")
            C.append(None)

    print(f"Lista A: {A}")
    print(f"Lista B: {B}")
    print(f"Operação de cada item: {C}")

def main():
    print("Escolha a operação:")
    print("1 - Converter negativos para positivos")
    print("2 - Produto cruzado dos vetores")
    escolha = input("Digite 1 ou 2: ")

    if escolha == '1':
        negativos_para_positivos()
    elif escolha == '2':
        produto_cruzado()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
