while True:
    numero_one = input("Oi Fernando, me manda um número: ")
    numero_two = input("Oi Fernando, me manda outro número: ")

    try:
        divisão = int(numero_one) / int(numero_two)
        print(f"A divisão dos dois números é: {divisão}")
    except ZeroDivisionError:
        print("Não pode dividir por 0")
    except ValueError:
        print("Coloca um número ué")