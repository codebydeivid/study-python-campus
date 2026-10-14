while True:
    number1 = input("Me fale um número: ")
    number2 = input("Me fale outro número: ")

    try:
        soma = int(number1) + int(number2)
        print(soma)
        break
    except ValueError:
        print("Você escreveu algo não numero tente novamente") 