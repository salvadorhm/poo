class Cadenas:

    cadena_1 = "hola4?"

    cadena_2 = "\u00BD"

    def __init__(self):
        pass


objeto = Cadenas()

print(objeto.cadena_1)
print(objeto.cadena_1.isalpha())
print(objeto.cadena_1.isalnum())

print(objeto.cadena_2)

print(objeto.cadena_2.isdecimal())
print(objeto.cadena_2.isdigit())
print(objeto.cadena_2.isnumeric())
