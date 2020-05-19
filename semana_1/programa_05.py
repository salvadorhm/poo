class TransporteTerrestre:

    def __init__(self):
        print("Constructor TransporteTerrestre")

    def acelerar(self):
        print("acelerar TransporteTerrestre")


class Coche(TransporteTerrestre):

    def __init__(self):
        print("Constructor Coche")

    def acelerar(self):
        print("acelerar Coche")

class Bicicleta(TransporteTerrestre):

    def __init__(self):
        print("Constructor Bicicleta")

    def acelerar(self):
        print("acelerar Bicicleta")
    

objeto_transporte_terrestre = TransporteTerrestre()
objeto_transporte_terrestre.acelerar()

objeto_coche = Coche()
objeto_coche.acelerar()

objeto_bicicleta = Bicicleta()
objeto_bicicleta.acelerar()

