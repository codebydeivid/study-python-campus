while True:
    valor = input("Me escreva um número: ")
    try:
        print(f"O número {int(valor)} é um número mesmo, obrigado :D")
        break
    except ValueError:
        print("(╯‵□′)╯︵┻━┻ Um número!!!")