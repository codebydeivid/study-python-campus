print("=" * 30)
print("SOMA ACUMULATIVA")
print("=" * 30)

numero = int(input("Digite um número: "))

if numero >= 0:
    contador = 0
    soma_total = 0
    sequencia = ""
    
    while contador <= numero:
        soma_total = soma_total + contador
        
        if contador == 0:
            sequencia = "0"
        else:
            sequencia = sequencia + " + " + str(contador)
        
        contador = contador + 1
    
    print(f"\nSoma de 0 até {numero}:")
    print(f"Sequência: {sequencia}")
    print(f"Resultado: {soma_total}")
else:
    print("Por favor, digite um número positivo.")

print("="*30 + "\n")