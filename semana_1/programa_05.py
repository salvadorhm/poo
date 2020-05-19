class TransporteTerrestre:

    def __init__(self):
        print("Constructor TransporteTerrestre")

    def acelerar(self):
        print("acelerar TransporteTerrestre")

class Coche(TransporteTerrestre):

    def __init__(self):
        print("Constructor Constructor")

    def acelerar(self):
        print("acelerar Coche")


objeto_transporte_terrestre = TransporteTerrestre()
objeto_transporte_terrestre.acelerar()

objeto_coche = Coche()
objeto_coche.acelerar()
