print("=" * 30)
print("CALCULADORA")
print("=" * 30)

continuar_calculadora = True

while continuar_calculadora:
    # Menu das operações
    print("\nEscolha a operação:")
    operacoes = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão", "5 - Sair"]
    
    for menu in operacoes:
        print(menu)
    
    # Escolha das operações
    opcao_operacao = input("Escolha uma operação (1-5): ")

    if opcao_operacao == "5":
        print("Saindo da calculadora...")
        continuar_calculadora = False
    elif opcao_operacao == "1" or opcao_operacao == "2" or opcao_operacao == "3" or opcao_operacao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao_operacao == "1":   
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif opcao_operacao == "2":
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif opcao_operacao == "3":
            resultado = num1 * num2
            print(f"\nResultado: {num1} × {num2} = {resultado}")
        elif opcao_operacao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} ÷ {num2} = {resultado:.2f}")
            else:
                print("\nErro: Divisão por zero não é possível >:(!")
    else:
        print("Opção inválida! Escolha uma opção de 1 a 5.")
        
print("="*30 + "\n")