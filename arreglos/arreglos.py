class Arreglos():

    datos = []

    def __init__(self):
        pass

    def leerArchivo(self):
        archivo = open("archivo.txt","r")
        for row in archivo:
            x = row.replace("\n", "")
            self.datos.append(x.split(","))

    def imprimirArreglo(self):
        for row in self.datos:
            print(row)

objeto = Arreglos()
objeto.leerArchivo()
objeto.imprimirArreglo()
print(objeto.datos[1][0])
