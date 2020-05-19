class Encapsulacion:

    variable_1 = 1   # public
    _variable_2 = 2  # protected
    __variable_3 = 3 # private

    def __init__(self):
        print(self.variable_1)
        print(self._variable_2)
        print(self.__variable_3)


objeto_encapsulacion = Encapsulacion()
print(objeto_encapsulacion.variable_1)
print(objeto_encapsulacion._variable_2)
print(objeto_encapsulacion.__variable_3)
