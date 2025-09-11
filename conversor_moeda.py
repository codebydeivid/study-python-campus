print("=" * 30)
print("CONVERSOR DE MOEDAS")
print("=" * 30)

cotacao_dolar = 5.529
cotacao_euro = 6.353

valor_reais = float(input("Digite o valor em reais (R$): "))

if valor_reais > 0:
    print("\nPara qual moeda deseja converter?")
    print("1 - Dólar (USD)")
    print("2 - Euro (EUR)")
    
    opcao_moeda = input("Digite sua opção (1 ou 2): ")
    
    if opcao_moeda == "1":
        valor_convertido = valor_reais / cotacao_dolar
        print(f"R$ {valor_reais:.2f} = US$ {valor_convertido:.2f}")
    elif opcao_moeda == "2":
        valor_convertido = valor_reais / cotacao_euro
        print(f"R$ {valor_reais:.2f} = € {valor_convertido:.2f}")
    else:
        print("Opção inválida! Digite 1 para Dólar ou 2 para Euro.")
else:
    print("Por favor, digite um valor positivo.")

print("="*30 + "\n")