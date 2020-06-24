class Archivos():

    def __init__(self):
        pass

    def leer(self, archivo):
        file = open(archivo, 'r')
        for line in file:
            print(line)
        file.close()

    def escribir(self, archivo, texto):
        file = open(archivo, 'w')
        texto = texto + "\n"
        file.write(texto)
        file.close()

objeto = Archivos()
objeto.leer("archivo.txt")
objeto.escribir("archivo.txt", "Este es un nuevo texto")
objeto.leer("archivo.txt")

