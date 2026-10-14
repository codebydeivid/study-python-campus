while True:
    nota = input("Qual a nota do aluno (de 0 a 10): ")
    try:
        if int(nota) < 0 or int(nota) > 10:
            raise Exception
        
        print(f"A nota dele é {nota}")
        break

    except ValueError:
        print("( ‵□′) Coloque um número")

    except Exception:
        print("Coloque uma nota de 0 a 10")