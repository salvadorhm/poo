class Arreglos():

    arreglo = []

    def __init__(self):
        pass

    def leer(self):
        archivo = open("archivo.txt","r")
        for row in archivo:
            self.arreglo.append(int(row))

    def imprimir(self):
        for row in self.arreglo:
            print(row)

    def promedio(self):
        total = 0
        for row in self.arreglo:
            total += row
        promedio_total = total / len(self.arreglo)
        print(promedio_total)

objeto = Arreglos()

objeto.leer()
objeto.imprimir()
objeto.promedio()