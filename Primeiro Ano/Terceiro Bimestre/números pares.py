print("=" * 30)
print("NÚMEROS PARES")
print("=" * 30)

limite = int(input("Digite um número de 0 a 20: "))

if limite >= 0 and limite <= 20:
    print(f"\nNúmeros pares de 0 até {limite}:")
    
    numero_atual = 0
    pares_encontrados = ""

    while numero_atual <= limite:
        if numero_atual % 2 == 0:
            if pares_encontrados == "":
                pares_encontrados = str(numero_atual)
            else:
                pares_encontrados = pares_encontrados + " - " + str(numero_atual)
        numero_atual = numero_atual + 1
    
    print(pares_encontrados)
else:
    print("Por favor, digite um número entre 0 e 20.")

print("="*30 + "\n")