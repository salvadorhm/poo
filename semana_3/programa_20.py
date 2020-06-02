class OperadoresAsignacion:

    def __init__(self):
        pass

    def operadores(self):
        variable = 10 # 10
        variable += 10 # 20
        variable -= 10 # 10
        variable *= 5 # 50
        variable /= 2 # 25
        variable %= 2 # 1
        variable //= 2 # 0
        print(variable)

objeto = OperadoresAsignacion()
objeto.operadores()
