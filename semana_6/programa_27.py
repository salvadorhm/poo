class Arreglos():

    arreglo = []

    def __init__(self):
        pass

    def agregarArreglo(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        z = int(input("Z: "))
        variable = [x, y, z]
        self.arreglo.append(variable)

    def imprimirArreglo(self):
        for row in self.arreglo:
            print(f"X: {row[0]} , Y: {row[1]}, Z: {row[2]}")

    
objeto = Arreglos()
for i in range(2):
    objeto.agregarArreglo()
objeto.imprimirArreglo()
