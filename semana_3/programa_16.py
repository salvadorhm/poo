class Cadenas:

    cadena = " Hola a todos bienvenidos al Curso "
    cadena_1 = "0.9"

    def __init__(self):
        pass

objeto = Cadenas()

print(objeto.cadena)
print(len(objeto.cadena)) # numero de caracteres
print(objeto.cadena.strip()) # quita los espcacios al inicio y al final
print(objeto.cadena.lower()) # convirte a minusculas
print(objeto.cadena.upper()) # converte a mayusculas

print(objeto.cadena.replace("o","0")) # remplaza caracteres
print(objeto.cadena.split(","))
