class Concatenar():

    def __init__(self):
        pass

    def concatenar(self, nombre, edad):
        persona = "Nombre {0}, Edad {1}".format(nombre, edad)
        return persona


objeto = Concatenar()

print(objeto.concatenar("Dejah", 25))
print(objeto.concatenar("Jhon", 27))
