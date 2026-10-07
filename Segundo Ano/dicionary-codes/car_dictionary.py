carDicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1946
}

print(carDicionario)
x = carDicionario["modelo"]
carDicionario["ano"] = 2018

print(f"\nO modelo do carro é: {x}")
print(f"O ano do carro é: {carDicionario['ano']}")
print(carDicionario)