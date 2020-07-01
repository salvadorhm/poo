class Ascii():

    def __init__(self):
        pass

    def ascii(self,caracter):
        return ord(caracter) #  Valor int del caracter

    def caracter(self, ascii):
        return chr(ascii) #  Convierte de Int a Caracter


objeto = Ascii()

print(objeto.ascii('0'))

print(objeto.caracter(92))
