class TipoDato:

    # Variables

    cadena = "Cadena" # str
    entero = 10 # int
    flotante = 13.5 # float
    compleja = 23j # complex
    booleana = True # bool

    def __init__(self):
        pass

objeto = TipoDato()

print(type(objeto.cadena))
print(type(objeto.entero))
print(type(objeto.flotante))
print(type(objeto.compleja))
print(type(objeto.booleana))
