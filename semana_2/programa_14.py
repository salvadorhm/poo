class Cadenas:

    cadena_1 = "Hola"
    cadena_2 = 'Hola'

    cadena_3 = """variable
cadena
de varias
lineas"""

    cadena_4 = '''Variable
cadena
de varias
lineas'''


    def __init__(self):
        pass


objeto = Cadenas()
print(objeto.cadena_1)
print(objeto.cadena_2)
print(objeto.cadena_3)
print(objeto.cadena_4)