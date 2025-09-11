print("=" * 30)
print("CONTAGEM REGRESSIVA")
print("=" * 30)

numero_inicial = int(input("Digite um número: "))

if numero_inicial >= 0:
    print(f"\nContagem regressiva de {numero_inicial} até 0:")
    
    contador_regressivo = numero_inicial
    sequencia_regressiva = ""
    
    while contador_regressivo >= 0:
        if contador_regressivo == numero_inicial:
            sequencia_regressiva = str(contador_regressivo)
        else:
            sequencia_regressiva = sequencia_regressiva + " -> " + str(contador_regressivo)
        
        contador_regressivo = contador_regressivo - 1
    print(sequencia_regressiva)
    
    if numero_inicial <= 10:
        print(f"\nDetalhamento:")
        print(f"Início: {numero_inicial}")
        print(f"Fim: 0")
        print(f"Total de números: {numero_inicial + 1}")
else:
    print("Por favor, digite um número positivo.")

print("="*30 + "\n")