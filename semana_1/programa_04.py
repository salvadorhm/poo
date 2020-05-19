class Coche:

    def __init__(self):
        print("Constructor de Coche")

    def acelerar(self):
        print("Acelerar")

    def frenar(self):
        print("Frenar")


class CocheRojo(Coche):

    def __init__(self):
        print("Constructor CocheRojo")

objeto = Coche()
objeto.acelerar()
objeto.frenar()

objeto_coche_rojo = CocheRojo()
objeto_coche_rojo.acelerar()
objeto_coche_rojo.frenar()

