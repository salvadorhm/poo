class Casting:

    # variables

    entera = 10 # int
    flotante = 12.56 # float
    cadena = "3" # str

    def __init__(self):
        pass

    def tipoDato(self):
        print("Tipos de datos")
        print(type(self.entera))
        print(type(self.flotante))
        print(type(self.cadena))

    def enteras(self):
        print("Enteros") # int()
        print(type(int(self.entera)))
        print(type(int(self.flotante)))
        print(type(int(self.cadena)))

    def flotantes(self):
        print("Flotantes") # float()
        print(type(float(self.entera)))
        print(type(float(self.flotante)))
        print(type(float(self.cadena)))

    def cadenas(self):
        print("Flotantes") # str()
        print(type(str(self.entera)))
        print(type(str(self.flotante)))
        print(type(str(self.cadena)))

objeto = Casting()
objeto.tipoDato()
objeto.enteras()
objeto.flotantes()
objeto.cadenas()
