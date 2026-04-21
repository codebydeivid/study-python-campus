from classes.ticketClass import MaquinaDeIngressos

# objetos
maquinaMeia=MaquinaDeIngressos(25)
maquinaInteira=MaquinaDeIngressos(50)
maquinaVIP=MaquinaDeIngressos(60)

maquinaInteira.definirPreco(10)
maquinaInteira.inserirDinheiro(80)

#maquinaInteira.imprimirIngresso()
maquinaMeia.imprimirIngresso()
maquinaVIP.imprimirIngresso()
