Filmes = {
    "nome": "Homem Aranha: Um Novo Dia",
    "ano": 2026,
    "diretor": "Destin Daniel Cretton",
    "nota": 10
}

print(f"O nome do filme é: {Filmes['nome']}")
print(f"O ano do filme é: {Filmes['ano']}")
print(f"O diretor do filme é: {Filmes['diretor']}")
print(f"A nota do filme é: {Filmes['nota']}")

Filmes.update({
    'genero': 'Ação, Super Herói, Comédia, Crise Existêncial', 
    'cineasta': 'Jon Watts'
    })

print(f"O genero do filme é: {Filmes['genero']}")
print(f"O cineasta do filme é: {Filmes['cineasta']}")