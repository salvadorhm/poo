class Arreglos():

    def __init__(self):
        pass

    def imprimirArreglo(self, arreglo):
        for elemento in arreglo:
            print(elemento)

    def insertarArreglo(self,arreglo, valor):
        arreglo.append(valor)

    def insertarArreglo2(self, arreglo):
        valor = raw_input("Dame un valor: ")
        arreglo.append(valor)

    def borrarArreglo(self, arreglo):
        arreglo.pop()

    def borrarArreglo2(self, arreglo, valor):
        arreglo.remove(valor)


objeto = Arreglos()
arreglo_0 = ["hola",False, 90, 34.6]
objeto.imprimirArreglo(arreglo_0)

objeto.borrarArreglo2(arreglo_0, False )
objeto.imprimirArreglo(arreglo_0)
