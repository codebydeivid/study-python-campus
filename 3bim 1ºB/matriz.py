# Leia uma matriz de 5x5 e verifique: – Qual o maior elemento da matriz e sua respectiva posição (linha e coluna). – Qual o menor elemento da matriz e sua respectiva posição (linha e coluna). – Qual a soma dos números da matriz. – Qual a média dos números da matriz.

def main():
    range_size = 3
    matriz = []
    for i in range(range_size):
        linha = []
        for j in range(range_size):
            try:
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
                return
        matriz.append(linha)

    maior = matriz[0][0]
    menor = matriz[0][0]
    pos_maior = (0, 0)
    pos_menor = (0, 0)
    soma = 0
    total_elementos = 0

    for i in range(range_size):
        for j in range(range_size):
            valor = matriz[i][j]
            soma += valor
            total_elementos += 1
            if valor > maior:
                maior = valor
                pos_maior = (i, j)
            if valor < menor:
                menor = valor
                pos_menor = (i, j)

    media = soma / total_elementos
    print(f"Maior elemento: {maior} na linha {pos_maior[0]} e na coluna {pos_maior[1]}")
    print(f"Menor elemento: {menor} na linha {pos_menor[0]} e na coluna {pos_menor[1]}")
    print(f"Soma dos elementos: {soma}")
    print(f"Média dos elementos: {media:.2f}")

if __name__ == "__main__": 
    main()