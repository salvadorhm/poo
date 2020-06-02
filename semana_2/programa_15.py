class Coche:

    # Atributos

    color = "Rojo"
    

    # Metodos

    def acelerar(self):
        print("Acelerar")

    def frenar(self):
        print("Frenar")

    def __init__(self):
        pass

class Tesla(Coche):

    # Atributos
    marca = "Tesla"
    duracion_baterias = "300 Km"

    # Metodos

    def estacionarseSolo(self):
        print("Estacionarse solo")

    def __init__(self):
        pass


model3 = Tesla()

print(model3.color)
print(model3.marca)
print(model3.duracion_baterias)

model3.acelerar()
model3.frenar()
model3.estacionarseSolo()
