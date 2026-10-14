try:
    print(x)
except NameError:
    print("Você errou aí")

try:
    y = "alo"
    print(y + 0)
except ValueError:
    print("Tá errado")

try:
        if list == 10:
         print(list)
except IndentationError:
    print("Cossoro")

try:
    dic = {
        "1": 34,
        "3": 445
    }
    print(dic["2"])
except KeyError:
    print("Turdo errado")

try:
    list = [1, 2 ,3 ,4]
    print(list[5])
except IndexError:
    print("Errrouuuuu")