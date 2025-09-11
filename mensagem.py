nome = input("Digite seu nome: ")

print("Bem-vindo ao chat! (Digite 'sair' para encerrar)")

def chat(name, msg):
    print(f"{name} > {msg}")

while True:
    mensagem = input(f"> ")
    print("-" * 40)
    chat(nome, mensagem)

    if mensagem.lower() == "sair":
        print("Saindo do chat. Até logo!")
        break