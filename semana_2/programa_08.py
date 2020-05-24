class Parametros:

    def __init__(self):
        pass

    def sumaDosNumeros(self, numero_1, numero_2):
        resultado = numero_1 + numero_2
        return resultado

    def restaDosNumeros(self, numero_1, numero_2):
        resultado = numero_1 - numero_2
        print(resultado)

objeto_parametros = Parametros()

resultado = objeto_parametros.sumaDosNumeros(3,7)
print(resultado)

print(objeto_parametros.sumaDosNumeros(4,8))

objeto_parametros.restaDosNumeros(6,3)