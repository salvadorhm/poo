class Variables:

    variable_global = "Global"

    def __init__(self):
        pass

    def variableLocal(self):
        variable_local = "Local"
        print(variable_local)


objeto_variables = Variables()
print(objeto_variables.variable_global)
objeto_variables.variableLocal()
