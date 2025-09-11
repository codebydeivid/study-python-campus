print("=" * 30)
print("CALCULADORA DE MÉDIA")
print("=" * 30 + "\n")
print("Digite algum número para calcular a média.")
print("Digite 'fim' quando quiser finalizar.\n")

soma_numeros = 0
quantidade_numeros = 0
continuar = True

while continuar:
    entrada = input("Digite um número (ou 'fim' para finalizar): ")
    
    if entrada.lower() == 'fim':
        continuar = False
    else:
        numero = float(entrada)
        soma_numeros = soma_numeros + numero
        quantidade_numeros = quantidade_numeros + 1
        print(f"Você adicionou o número {numero} - Quantidade de números: {quantidade_numeros}")

if quantidade_numeros > 0:
    media = soma_numeros / quantidade_numeros
    print(f"\nQuantidade de números: {quantidade_numeros}")
    print(f"Soma total: {soma_numeros}")
    print(f"Média: {media:.2f}")
else:
    print("Você saiu, nenhum número foi inserido.")

print("\n" + "="*30)