class Formato():

    def __init__(self):
        pass

    def formatear(self, nombre, edad):
        persona = f"Nombre: {nombre}, Edad: {edad}"
        return persona

objeto = Formato()

print(objeto.formatear("Dejah", 25))
print(objeto.formatear("Jhon", 27))

