
def lista_num():
    # Crie uma função que some uma lista de números
    import random
    lista = []

    def somar_lista(lista):
        tamanho = len(lista)
        soma = 0
        for i in range(0, tamanho):
            soma += lista[i]
        return soma

    def preencher_lista(lista):
        for i in range(0, 10):
            lista.append(random.randint(1, 100))
        return lista
    
    def print_bnt(arg):
        print("_" * 30)
        print(arg)
        print("-" * 30)

    print_bnt("Somando números na lista")
    preencher_lista(lista)
    print(f"Soma dos números na lista: {somar_lista(lista)}")
    print(f"Lista de números somados: {lista} \n")

    main()
def maior_valr():
    #Crie uma função para encontrar o maior valor de uma lista
    import random
    lista = []
    def maior_valor(lista):
        tamanho = len(lista)
        maior = lista[0]
        for i in range(0, tamanho):
            if lista[i] > maior:
                maior = lista[i]
        return maior
    
    def preencher_lista(lista):
        for i in range(0, 10):
            lista.append(random.randint(1, 100))
        return lista

    def print_bnt(arg):
        print("_" * 30)
        print(arg)
        print("-" * 30)

    preencher_lista(lista)
    print_bnt("Descobrindo o maior valor na lista")
    print(f"O maior valor na lista é: {maior_valor(lista)}")
    print(f"Lista de números: {lista} \n")

    main()

def palindromo():
    #Escreva uma função para verificar se uma palavra é palíndromo (palíndromo é uma palavra que tem o mesmo significado quando é lido da direita para esquerda, ex: arara ou mirim).
    def verificar_palindromo(palavra):
        palavra_invertida = palavra[::-1]
        if palavra == palavra_invertida:
            return True
        else:
            return False
    
    def print_bnt(arg):
        print("_" * 30)
        print(arg)
        print("-" * 30)

    print_bnt("Verificando se a palavra é palíndromo")
    palavra = input("Digite uma palavra e descubra se é palíndromo: ")
    if verificar_palindromo(palavra):
        print(f"~ A palavra '{palavra}' é um palíndromo. ~\n")
    else:  
        print("~ A palavra não é um palíndromo. ~\n")

    main()
def palindromo2():
    def verificar_palindromo(palavra):
        tamanho = len(palavra)
        for i in range(tamanho // 2):
            if palavra[i] != palavra[tamanho - 1 - i]:
                return False
        return True
    
    def print_bnt(arg):
        print("_" * 30)
        print(arg)
        print("-" * 30)

    print_bnt("Verificando se a palavra é palíndromo")
    palavra = input("Digite uma palavra e descubra se é palíndromo: ")
    if verificar_palindromo(palavra):
        print(f"~ A palavra '{palavra}' é um palíndromo. ~\n")
    else:  
        print("~ A palavra não é um palíndromo. ~\n")
    
    main()

def main():
    print("Qual você quer rodar?")
    print("1- Soma lista de número")
    print("2- Maior valor de uma lista")
    print("3- É palindromo?")
    print("4- Sair")

    resposta = int(input("-> "))
    if resposta == 1:
        lista_num()
    elif resposta == 2:
        maior_valr()
    elif resposta == 3:
        palindromo2()
    else:
        print("Você saiu!")

main()