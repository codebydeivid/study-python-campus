while True:
    x = 10
    numero = input("Coloque um número: ")
    soma = x + int(numero)
    
    try:   
        if soma > 1000:
            raise Exception
        else:
            print(soma)
            break
    except:
        print("Deu errado aqui")