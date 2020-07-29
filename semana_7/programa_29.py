class Diccionarios():

    persona = {'nombre':'Dejah','edad':25, 'email':'dejah@email.com'}

    def __init__(self):
        pass

    def imprimirLlaves(self, diccionario):
        for key in diccionario:
            print(key)

    def imprimirValores(self, diccionario):
        for key in diccionario:
            print(diccionario[key])

    def insertarValor(self, diccionario, key, value):
        diccionario[key] = value

    def modificarValor(self,diccionario, key, value):
        diccionario[key] = value

    def quitarValor(self,diccionario, key):
        diccionario.pop(key)
    
objeto = Diccionarios()
#objeto.imprimirLlaves(objeto.persona)
#objeto.insertarValor(objeto.persona, "ciudad", "Hidalgo")
objeto.imprimirValores(objeto.persona)
#objeto.modificarValor(objeto.persona,"edad",23)
objeto.quitarValor(objeto.persona, "email")
objeto.imprimirValores(objeto.persona)


