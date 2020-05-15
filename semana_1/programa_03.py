class VariablesGlobales:

    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        print(self.nombre)

objeto_0 = VariablesGlobales("Salvador")
objeto_0.getNombre()

objeto_1 = VariablesGlobales("Dejah")
objeto_1.getNombre()
