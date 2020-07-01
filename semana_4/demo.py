class Demo():

    def __init__(self):
        pass

    def leer(self):
        archivo = open("archivo.txt","r") # r - read - leer
        for linea in archivo:
            print(linea) # codigo para cifrar o descifrar
        archivo.close()

    def escribir(self):
        archivo = open("archivo.txt","a") # a - append - agregar
        texto = input("Escribe un texto: ")
        archivo.write(texto + "\n")
        archivo.close()

objeto = Demo()
objeto.escribir()


